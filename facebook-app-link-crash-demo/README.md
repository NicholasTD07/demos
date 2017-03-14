# Facebook app link crash demo and its fix

## How to use this project?

to reproduce the crash and verify the fix

1. Clone it
2. Run `pod install`
3. Open the workspace
4. Compile and run the app
5. Expect to see no crash
6. Edit `Podfile`: change line 16 from `not_crashing` to `crashing`
7. Repeat steps 2 to 4
8. Expect to see the app crash

## What causes the crash?

In `AppDelegate.swift`, we are trying to use `FBSDKApplicationDelegate.application(_:open:sourceApplication:annotation:)` to open an URL that contains a JSON string like this:

```json
{"target_url": null, "extras": {"fb_app_id": 12345}}
```

## Why does FBCoreKit crash?

In the app links (see `AppDelegate.swift` for example), the value of `target_url` in the JSON string can be
`null`.  After decoding the JSON string, `target_url` will be decoded
into an `NSNull`.

FBSDKCoreKit will crash when trying to create an 
`NSURL` from `NSNull` and thus crash the app.
