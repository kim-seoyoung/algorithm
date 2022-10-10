class Solution:
    def isPalindrome(self, str_input:str) -> bool:
        len_input = len(str_input)
        if len_input <2:
            return True
        elif len_input == 2:
            if str_input[0] == str_input[1]:
                return True
            else:
                return False
        else:
            start_p = 0
            end_p = len_input-1
            while start_p < end_p:
                if str_input[start_p] == str_input[end_p]:
                    start_p += 1
                    end_p -= 1
                else:
                    return False
            return True
        
    def breakPalindrome(self, palindrome: str) -> str:
        len_pal = len(palindrome)
        for replace in range(97, 123):
            replace_letter = chr(replace)
            
            for i in range(len_pal):
                save_letter = palindrome[i]
                if ord(save_letter) < ord(replace_letter) and i < len_pal -1:
                    continue
                else:
                    tmp = list(palindrome)
                    tmp[i] = replace_letter
                    palindrome = ''.join(tmp)
                    if not self.isPalindrome(palindrome):
                        return palindrome
                    else:
                        tmp = list(palindrome)
                        tmp[i] = save_letter
                        palindrome = ''.join(tmp)
        return ""
                    