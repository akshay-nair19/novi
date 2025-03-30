//
//  WardrobeView.swift
//  Novi
//
//  Created by Ashton Ma on 3/30/25.
//

import SwiftUI

// Assuming `Clothing`, `Shirt`, `Pant`, `Wardrobe` are defined as you mentioned before
struct WardrobeView: View {
    @StateObject private var wardrobe = Wardrobe() // Use @StateObject to observe changes
    @State private var history = History()
    
    @State private var selectedShirt: Shirt? = nil
    @State private var selectedPant: Pant? = nil
    @State private var showingAddItemView = false
    
    // Define the filtered lists explicitly
    private var shirts: [Shirt] {
        wardrobe.getItems().compactMap { $0 as? Shirt }
    }
    
    private var pants: [Pant] {
        wardrobe.getItems().compactMap { $0 as? Pant }
    }
    
    var body: some View {
        NavigationView {
            VStack {
                // Shirts Selection Section
                Text("Select Shirt")
                    .font(.headline)
                    .padding(.top)
                
                // Displaying shirts in horizontal scroll view
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack {
                        ForEach(shirts, id: \.id) { shirt in
                            Button(action: {
                                self.selectedShirt = shirt
                            }) {
                                Text(shirt.color)
                                    .padding()
                                    .background(self.selectedShirt == shirt ? Color.blue : Color.gray)
                                    .foregroundColor(.white)
                                    .cornerRadius(10)
                            }
                            .padding(5)
                        }
                    }
                }
                
                // Pants Selection Section
                Text("Select Pant")
                    .font(.headline)
                    .padding(.top)
                
                // Displaying pants in horizontal scroll view
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack {
                        ForEach(pants, id: \.id) { pant in
                            Button(action: {
                                self.selectedPant = pant
                            }) {
                                Text(pant.color)
                                    .padding()
                                    .background(self.selectedPant == pant ? Color.blue : Color.gray)
                                    .foregroundColor(.white)
                                    .cornerRadius(10)
                            }
                            .padding(5)
                        }
                    }
                }
                
                // Button to wear the selected outfit
                Button("Wear Outfit") {
                    if let shirt = selectedShirt, let pant = selectedPant {
                        history.wearOutfit(shirt: shirt, pant: pant)
                        print("Wore Outfit: Shirt(\(shirt.color), \(shirt.picture)) - Pant(\(pant.color), \(pant.picture))")
                    }
                }
                .padding()
                .background(Color.blue)
                .foregroundColor(.white)
                .cornerRadius(10)
                .padding(.top)
                
                // Button to show history
                Button("Show History") {
                    history.printHistory()
                }
                .padding(.top)
            }
            .navigationBarTitle("Wardrobe")
            .navigationBarItems(trailing: Button(action: {
                showingAddItemView = true
            }) {
                Image(systemName: "plus")
                    .font(.title)
            })
            .sheet(isPresented: $showingAddItemView) {
                AddItemView(wardrobe: $wardrobe)
            }
        }
    }
}
