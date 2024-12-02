import Foundation

do {
    var file_str: String = ""
    let file = try Data(contentsOf: URL(filePath: "./input1_1"))
    file.forEach() { char in
        file_str += String(Character(UnicodeScalar(char)))
    }

    let num_pair_arr = file_str.components(separatedBy: "\n")

    var arrl = [Int]()
    var arrr = [Int]()
    
    for num_pair in num_pair_arr {
        let split_num_pair = num_pair.components(separatedBy: "   ")
        if split_num_pair[0] == "" { break }
        arrl.append(Int(split_num_pair[0])!)
        arrr.append(Int(split_num_pair[1])!)
    }

    arrl.sort()
    arrr.sort()

    var total: Int = 0

    for i in 0...arrl.count-1 {
        total += abs(arrl[i] - arrr[i])
    }

    print(total)
   
} catch {
    print("Error reading file: \(error)")
}


