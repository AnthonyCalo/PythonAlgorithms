// Input: s = "hello"
// Output: "holle"

/**
 * @param {string} s
 * @return {string}
 */
 var reverseVowels = function(s) {
    let vowels=['a','e','i','o', 'u',"A","E","I","O","U"]

    let vow_locs=[]
    for(var i =0;i<s.length;i++){
        if(vowels.includes(s[i])){
            vow_locs.push(s[i])
        }
    }
    let return_s=[]
    for(var j=0; j<s.length;j++){
        if(vowels.includes(s[j])){
            return_s.push(vow_locs.pop())
        }else{
            return_s.push(s[j])
        }
    }
    return( return_s.join(""))

};