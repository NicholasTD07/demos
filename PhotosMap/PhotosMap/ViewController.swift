//
//  ViewController.swift
//  PhotosMap
//
//  Created by Nicholas Tian on 13/6/17.
//  Copyright © 2017 nickTD. All rights reserved.
//

import UIKit
import Photos
import MapKit

class ViewController: UIViewController {
    @IBOutlet var mapView: MKMapView!

    override func viewDidLoad() {
        super.viewDidLoad()

        let assets = PHAsset.fetchAssets(with: .image, options: PHFetchOptions())

        print(assets.count)

        assets.enumerateObjects { (asset, _, _) in
            guard let coordinate = asset.location?.coordinate else { return }

            let placemark = MKPlacemark(coordinate: coordinate)

            self.mapView.addAnnotation(placemark)
        }
    }
}
