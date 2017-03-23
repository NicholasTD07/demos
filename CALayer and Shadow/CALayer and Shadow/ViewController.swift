//
//  ViewController.swift
//  CALayer and Shadow
//
//  Created by Nicholas Tian on 22/03/2017.
//  Copyright © 2017 nicktd. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.

        setupView()
    }

    private func setupView() {
        let redView = UIView(frame: CGRect(x: 100, y:100, width: 100, height: 100))
        redView.backgroundColor = .red

        view.addSubview(redView)

        let layer = redView.layer

        layer.shadowOpacity = 0.3 // shows the shadow
        // layer.shadowOffset = CGSize(width:0, height: 3) // moves the shadowCGC
        let path = CGPath(rect: CGRect(x: layer.bounds.origin.x - 20, y: layer.bounds.origin.y + layer.bounds.height, width: layer.bounds.width + 2 * 20, height: 10), transform: nil)
        layer.shadowPath = path
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

