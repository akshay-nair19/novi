//
//  AddItemView.swift
//  Novi
//
//  Created by Ashton Ma on 3/30/25.
//


import SwiftUI

struct AddItemView: View {
    @Environment(\.presentationMode) var presentationMode
    @Binding var wardrobe: Wardrobe
    @State private var selectedItem: String = "Shirt" // Default item to add
    @State private var selectedColor: String = "" // Color input
    @State private var selectedSize: String = "" // Size input
    
    var body: some View {
        VStack {
            Text("Add New Item")
                .font(.title)
                .padding()
            
            // Picker for Shirt or Pant
            Picker("Select Item Type", selection: $selectedItem) {
                Text("Shirt").tag("Shirt")
                Text("Pant").tag("Pant")
            }
            .pickerStyle(SegmentedPickerStyle())
            .padding()
            
            // Color input field
            TextField("Enter Color", text: $selectedColor)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            
            // Size input field
            TextField("Enter Size", text: $selectedSize)
                .textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
            
            Button("Add \(selectedItem)") {
                if !selectedColor.isEmpty && !selectedSize.isEmpty {
                    let item = createNewItem()
                    wardrobe.addItem(item)
                    presentationMode.wrappedValue.dismiss() // Go back to the previous screen
                }
            }
            .padding()
            .background(Color.blue)
            .foregroundColor(.white)
            .cornerRadius(10)
            .padding()
        }
        .padding()
    }
    
    func createNewItem() -> Clothing {
        if selectedItem == "Shirt" {
            return Shirt(color: selectedColor, picture: "shirt_image", size: selectedSize)
        } else {
            return Pant(color: selectedColor, picture: "pant_image", size: selectedSize)
        }
    }
}

