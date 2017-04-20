import os
import glob
import datetime


def directories_in(directory):
    return glob.glob(os.path.join(directory, "*/"))

def changed_at_for(directory, filename=None):
    gettime = os.path.getmtime
    if filename:
        return gettime(os.path.join(directory, filename))
    else:
        return gettime(directory)

def changed_at_for_minecraft_save(save):
    return changed_at_for(save, filename='level.dat')

def date_string_for(timestamp):
    date = datetime.datetime.fromtimestamp(timestamp)
    return date.strftime("D-%Y-%m-%d-T-%H-%M-%S")

if __name__ == '__main__':
    saves = directories_in('/vagrant/backups/')

    save_and_time = [
        (save, changed_at_for_minecraft_save(save))
        for save in saves
    ]

    sorted_save_and_time = sorted(save_and_time, cmp=lambda a, b: int(a[1] - b[1]))
    # for (save, time) in sorted_save_and_time:
    #     print(save)
    #     print(date_string_for(time))

    copy_command_template = 'cp -rv {} /test/snapshots/the_world'
    def copy_command_for(save):
        return ['cp', '-rv', save, '/test/snapshots/the_world']
    snapshot_template = "sudo zfs snapshot test/snapshots@{}"

    import subprocess
    for (save, time) in sorted_save_and_time:
        copy = copy_command_for(save)
        print("Running {}").format(' '.join(copy))
        output = subprocess.check_output(copy)
        output = output or ""
        print(output)

        snapshot = snapshot_template.format(date_string_for(time))
        print("Running {}").format(snapshot)
        output = subprocess.check_output(snapshot.split(' '))
        output = output or ""
        print(output)
