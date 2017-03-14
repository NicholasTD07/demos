//
//  AppDelegate.swift
//  facebook-app-link-crash-demo
//
//  Created by Nicholas Tian on 14/03/2017.
//  Copyright © 2017 nicktd. All rights reserved.
//

import UIKit
import FBSDKCoreKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?


    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
        let URLString = "dev.nicktd.com?al_applink_data=%7B%22target_url%22%3Anull%2C%22extras%22%3A%7B%22fb_app_id%22%3A12345%7D%7D"
        let aURL = URL(string: URLString)!

        FBSDKApplicationDelegate.sharedInstance().application(application, open: aURL, sourceApplication: "demo", annotation: "")

        return true
    }

}

