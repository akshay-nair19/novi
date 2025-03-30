//
//  WardrobeClasses.swift
//  Novi
//
//  Created by Ashton Ma on 3/30/25.
//

import SwiftUI
import Foundation

class Clothing: Identifiable {
    var id = UUID() // Unique identifier
    var color: String
    var picture: String
    var size: String
    
    init(color: String, picture: String, size: String) {
        self.color = color
        self.picture = picture
        self.size = size
    }
}

class Shirt: Clothing {
    override init(color: String, picture: String, size: String) {
        super.init(color: color, picture: picture, size: size)
    }
}

class Pant: Clothing {
    override init(color: String, picture: String, size: String) {
        super.init(color: color, picture: picture, size: size)
    }
}



// Mark Wardrobe as ObservableObject so the view updates when items are added
class Wardrobe: ObservableObject {
    @Published var items: [Clothing] = [] // Mark items as @Published
    
    func addItem(_ item: Clothing) {
        items.append(item)
    }
    
    func addMultipleItems(_ items: [Clothing]) {
        self.items.append(contentsOf: items)
    }
    
    func removeItem(_ item: Clothing) {
        if let index = items.firstIndex(where: { $0.id == item.id }) {
            items.remove(at: index)
        }
    }
    
    func getItems() -> [Clothing] {
        return items
    }
}


class History {
    private var history: [(Shirt, Pant)] = []
    
    func wearOutfit(shirt: Shirt, pant: Pant) {
        if history.count >= 7 {
            history.removeFirst()
        }
        history.append((shirt, pant))
    }
    
    func printHistory() {
        for (index, outfit) in history.enumerated() {
            print("Outfit \(index + 1): Shirt(\(outfit.0.color), \(outfit.0.picture)) - Pant(\(outfit.1.color), \(outfit.1.picture))")
        }
    }
}
