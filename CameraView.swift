//
//  CameraView.swift
//  Novi
//
//  Created by Ashton Ma on 3/29/25.
//


import SwiftUI
import AVFoundation
import PhotosUI
import Foundation



struct CameraView: UIViewControllerRepresentable {
    
    @Binding var image: UIImage? // bind to the parent view's state
    @Environment (\.presentationMode) var presentationMode // Dismiss the view when done
    
    func makeUIViewController(context: Context) -> UIImagePickerController {
        let picker = UIImagePickerController() // create the camera picker
        picker.delegate = context.coordinator // set the coordinator as delegate
        picker.sourceType = .camera  // set the source to the camera
        return picker
    }
    
    func updateUIViewController(_ uiViewController: UIImagePickerController, context: Context) {
        // NO updates needed
    }
    
    func makeCoordinator() -> Coordinator {
        Coordinator(self)
    }
    
    class Coordinator: NSObject, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
        let parent: CameraView
        
        init(_ parent: CameraView){
            self.parent = parent
        }
        func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
            if let image = info[.originalImage] as? UIImage {
                parent.image = image // pass the selected image to the parent
            }
            parent.presentationMode.wrappedValue.dismiss() //dismiss the picker
        }
        func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
            parent.presentationMode.wrappedValue.dismiss()//dismiss on cancel
        }
    }
    
}



//struct CameraView: UIViewControllerRepresentable {
//    func makeUIViewController(context: Context) -> CameraManager {
//        return CameraManager()
//    }
//    
//    func updateUIViewController(_ uiViewController: CameraManager, context: Context) {
//        // No updates needed
//    }
//}
