//
//  UploadPicture.swift
//  Novi
//
//  Created by Ashton Ma on 3/30/25.
//

import SwiftUI
import PhotosUI



struct UploadView: View {
    @State private var selectedItem: PhotosPickerItem? // holds the selected photo item
    @State private var selectedImage: UIImage? // holds the loaded image
    @State private var showingCamera = false // control camera visibility
    
    var body: some View {
        VStack {
            // display the selected image or placeholder
            if let selectedImage = selectedImage {
                Image(uiImage: selectedImage)
                    .resizable()
                    .scaledToFit()
                    .frame(height: 500)
                    .cornerRadius(25)
            }else {
                Text("No Image Selected")
                    .foregroundStyle(Color.gray)
                    .padding()
            }
            
            Button(action: {
                showingCamera = true // show the camera view
            }){
                Text("Take Photo")
                    .font(.headline)
                    .padding()
            }
            .sheet(isPresented: $showingCamera){
                CameraView(image: $selectedImage)
            }
            
            
            //photo picker button
            PhotosPicker(selection: $selectedItem, matching: .images, photoLibrary: .shared()) {
                Text("Select Photo")
                    .font(.headline)
            }
            .onChange(of: selectedItem){
                newItem in
                //handle the selected item
                if let newItem = newItem{
                    Task{
                        if let data = try? await newItem.loadTransferable(type: Data.self), let image = UIImage(data:data){
                            selectedImage = image
                        }
                    }
                }
            }
        }
        .padding()
    }
}
