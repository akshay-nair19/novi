//
//  ContentView.swift
//  Novi
//
//  Created by Ashton Ma on 3/29/25.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {
            VStack {
                // NavigationLink for Camera Button
                NavigationLink(destination: UploadView()) {
                    Text("Upload Image")
                        .font(.title)
                        .padding()
                        .background(Color.blue)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                }
                
                // NavigationLink to Next Page
                NavigationLink(destination: WardrobeView()) {
                    Text("Wardrobe")
                        .font(.title)
                        .padding()
                        .background(Color.green)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                }
            }
            .navigationTitle("Home")
        }
    }
}




#Preview {
    ContentView()
}
