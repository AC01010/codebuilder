# Codebuilder [BETA]
Automates creating a Codebusters test for Science Olympiad practice. Outputs a json file that can be imported directly to Toebes.

This program pulls quotes from a database of 40000+ quotes. All ciphers for use in the 2020-2021 season, with the exception of keyed monoalphabetic substitution ciphers (K1/K2), have been implemented.

**Disclaimer: This program is only for practice. If you are an event supervisor, tournament director, or any test writer, you may not use Codebuilder to generate tests for use in any sanctioned competition, including invitationals, regionals, or state competitions. In addition, you may not use Codebuilder for any test exchanges, such as SSSS, Captains Test Exchange, or anywhere where the test will be publicly released without my permission.**

If you would like to request new features or report any bugs, feel free to create an issue; however, chances are I won't get to it.

### Presets ###
Currently, there are four presets:

1.  **All Types** - 29 Questions + Timed - Includes one of each cipher type.
    - 1 Timed Question
    - 1 Unhinted Aristocrat
    - 1 Character-Hinted Aristocrat
    - 1 Word-Hinted Aristocrat
    - 1 Unhinted Patristocrat
    - 1 Character-Hinted Patristocrat
    - 1 Word-Hinted Patristocrat
    - 1 Affine Decode
    - 1 Affine Encode
    - 1 Affine Cryptanalysis
    - 1 Caesar Decode
    - 1 Caesar Encode
    - 1 Vigenere Decode
    - 1 Vigenere Encode
    - 1 Vigenere Cryptanalysis
    - 1 2x2 Hill Compute Decryption Matrix
    - 1 2x2 Hill Decode
    - 1 2x2 Hill Encode
    - 1 3x3 Hill Decode
    - 1 3x3 Hill Encode
    - 1 Xenocrypt
    - 1 Bacon Letter for Letter
    - 1 Bacon Sequential
    - 1 Bacon Words
    - 1 RSA Euclid
    - 1 RSA Exponentiation
    - 1 Morbit Decrypt
    - 1 Morbit Cryptanalysis
    - 1 Pollux Decrypt
    - 1 Pollux Cryptanalysis
   
2.  **National Level Test** - 30 Questions + Timed - National level test, with random modes of questions.
    - 1 Timed Question
    - 10 Unhinted Aristocrats
    - 1 Unhinted Patristocrat
    - 1 Character-Hinted Patristocrat
    - 1 Word-Hinted Patristocrat
    - 2 Affine 
    - 1 Caesar Decode
    - 1 Caesar Encode
    - 2 Vigenere
    - 3 Hill
    - 1 Xenocrypt
    - 2 Bacon
    - 2 RSA
    - 3 Morse

3.  **Regional Level Test** - 19 Questions + Timed - Regional level test, with random modes of questions.
    - 1 Timed Question
    - 4 Unhinted Aristocrats
    - 1 Character-Hinted Aristocrat
    - 1 Word-Hinted Aristocrat
    - 1 Unhinted Patristocrat
    - 1 Word-Hinted Patristocrat
    - 1 Affine Decode
    - 1 Caesar Decode
    - 1 Vigenere Decode
    - 1 2x2 Hill Decode
    - 2 Encode (Affine/Caesar/Vigenere/2x2 Hill)
    - 1 Xenocrypt
    - 2 Bacon
    - 1 Morbit Decrypt
    - 1 Pollux Decrypt
    
4.  **Aristo Spam** - 10 Questions + Timed - 10 Unhinted Aristocrats.
    - 1 Timed Question
    - 10 Unhinted Aristocrats
    
5.  **Patristo Spam** - 10 Questions + Timed - 10 Unhinted Patristocrats.
    - 1 Timed Question
    - 10 Unhinted Patristocrats
    
6.  **Custom** - Custom made test.

Codebuilder Discord Bot:
**Invite Link:** https://discord.com/api/oauth2/authorize?client_id=787535889135828994&permissions=125952&scope=bot

Commands:
    - `c!gen \[Name] \[Preset]` - `c!gen example 1`
    - `c!genCustom \[Name] \[Custom Question List]` - `c!gen example "1 2,3 1,8 0"
    - `c!fetch \[Name]` - `c!fetch example`
    - 
