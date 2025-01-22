// Hawaiian Words Project - Maya Thomas-Fubler

#include <iostream>
#include <cctype>
#include <string>

using namespace std; 

int main() 
{
  char yesno = 'Y'; 

  while (yesno == 'Y')
    {
      const int SIZE = 100;
      char word[SIZE]; 

      cout << "Enter a Hawaiian word to pronounce: " << endl;
      cin.getline(word, SIZE);
      cout << endl; 

      cout << word << " is pronounced: ";

      for (int x = 0; word[x] != '\0'; x++)
      {
        word[x] = tolower(word[x]);

        if (word[x] != 'p' && word[x] != 'k' && word[x] != 'h' && word[x] != 'l' && word[x] != 'm' && word[x] != 'n' && word[x] != 'w' && word[x] != 'a' && word[x] != 'e' && word[x] != 'i' && word[x] != 'o' && word[x] != 'u' && word[x] != '\'' && word[x] != ' ')
        {
          cout << "Error. Word is either not a valid Hawaiian word or contains an invalid character." << endl; 
          cout << endl; 
          cout << endl;
          break;  
          }

        //This is where the evalulation for each letter will be. 
       //Consontants 
       if (word[x] == 'p')
       {
         cout << "p";
         continue;
       }

      if (word[x] == 'k')
      {
        cout << "k";
        continue;
      }


      if (word[x] == 'h')
      {
        cout << "h";
        continue;
      }

      if (word[x] == 'l')
      {
        cout << "l";
        continue;
      }

      if (word[x] == 'm')
      {
        cout << "m";
        continue;
      }

      if (word[x] == 'n')
      {
        cout << "n";
        continue;
      }

      if (word[x] == 'w')
      {
        int y = x - 1;
        if (word[y] == 'i' || word[y] == 'e' )
          cout << "v";

        else 
          cout << "w";

        continue;
      }

       //Vowels & Groups

       // Letter A 
        int z = x + 1;

         if (word[x] == 'a' && (word[z] == 'i' || word[z] == 'e'))
          {
            cout << "eye";
            x++;

            int h = x + 1; 
            if (word[h] == ' ') 
            {
              cout << " ";
              continue;
            }
            if (word[h] == '\'' || word[h] == '\0') 
              {
                cout << "";
                continue;
              }
            else
              {
                cout << "-";
                continue;
              }

            continue;

          }

         if (word[x] == 'a' && (word[z] == 'o' || word[z] == 'u'))
            {
             cout << "ow";   
             x++;

              int h = x + 1; 
              if (word[h] == ' ') 
              {
                cout << " ";
                continue;
              }
              if (word[h] == '\'' || word[h] == '\0') 
                {
                  cout << "";
                  continue;
                }
              else
                {
                  cout << "-";
                  continue;
                }

              continue;
           }

        if (word[x] == 'a')
        {
          cout << "ah"; 

          int h = x + 1; 
          if (word[h] == ' ') 
          {
            cout << " ";
            continue;
          }
          if (word[h] == '\'' || word[h] == '\0') 
            {
              cout << "";
              continue;
            }
          else
            {
              cout << "-";
              continue;
            }

          continue;
        }

        // Letter E
        if (word[x] == 'e' && word[z] == 'i')
          {
            cout << "ay";
            x += 1;

            int h = x + 1; 
            if (word[h] == ' ') 
            {
              cout << " ";
              continue;
            }
            if (word[h] == '\'' || word[h] == '\0') 
              {
                cout << "";
                continue;
              }
            else
              {
                cout << "-";
                continue;
              }

            continue;
          }

         if (word[x] == 'e' && word[z] == 'u')
            {
             cout << "eh-oo";
             x += 1;

              int h = x + 1; 
              if (word[h] == ' ') 
              {
                cout << " ";
                continue;
              }
              if (word[h] == '\'' || word[h] == '\0') 
                {
                  cout << "";
                  continue;
                }
              else
                {
                  cout << "-";
                  continue;
                }

              continue;
           }

        if (word[x] == 'e')
        {
          cout << "eh";

          int h = x + 1; 
          if (word[h] == ' ') 
          {
            cout << " ";
            continue;
          }
          if (word[h] == '\'' || word[h] == '\0') 
            {
              cout << "";
              continue;
            }
          else
            {
              cout << "-";
              continue;
            }

          continue;
        }

        // Letter I
        if (word[x] == 'i' && word[z] == 'u')
          {
            cout << "ew";
            x += 1;

            int h = x + 1; 
            if (word[h] == ' ') 
            {
              cout << " ";
              continue;
            }
            if (word[h] == '\'' || word[h] == '\0') 
              {
                cout << "";
                continue;
              }
            else
              {
                cout << "-";
                continue;
              }

            continue;

          }

        if (word[x] == 'i')
        {
          cout << "ee";

          int h = x + 1; 
          if (word[h] == ' ') 
          {
            cout << " ";
            continue;
          }
          if (word[h] == '\'' || word[h] == '\0') 
            {
              cout << "";
              continue;
            }
          else
            {
              cout << "-";
              continue;
            }

          continue;
        }

        // Letter O
        if (word[x] == 'o' && word[z] == 'i')
          {
            cout << "oy";
            x += 1;

            int h = x + 1; 
            if (word[h] == ' ') 
            {
              cout << " ";
              continue;
            }
            if (word[h] == '\'' || word[h] == '\0') 
              {
                cout << "";
                continue;
              }
            else
              {
                cout << "-";
                continue;
              }

            continue;

          }

         if (word[x] == 'o' && word[z] == 'u')
            {
             cout << "ow";
            // cout << "-";
             x += 1;

              int h = x + 1; 
              if (word[h] == ' ') 
              {
                cout << " ";
                continue;
              }
              if (word[h] == '\'' || word[h] == '\0') 
                {
                  cout << "";
                  continue;
                }
              else
                {
                  cout << "-";
                  continue;
                }

              continue;
           }

        if (word[x] == 'o')
        {
          cout << "oh";

          int h = x + 1; 
          if (word[h] == ' ') 
          {
            cout << " ";
            continue;
          }
          if (word[h] == '\'' || word[h] == '\0') 
            {
              cout << "";
              continue;
            }
          else
            {
              cout << "-";
              continue;
            }

          continue;
        }

        // Letter U 
        if (word[x] == 'u' && word[z] == 'i')
          {
            cout << "ooey";
            x += 1;

            int h = x + 1; 
            if (word[h] == ' ') 
            {
              cout << " ";
              continue;
            }
            if (word[h] == '\'' || word[h] == '\0') 
              {
                cout << "";
                continue;
              }
            else
              {
                cout << "-";
                continue;
              }

            continue;

          }

        if (word[x] == 'u')
        {
          cout << "oo";

          int h = x + 1; 
          if (word[h] == ' ') 
          {
            cout << " ";
            continue;
          }
          if (word[h] == '\'' || word[h] == '\0') 
            {
              cout << "";
              continue;
            }
          else
            {
              cout << "-";
              continue;
            }

          continue;
        }

        if (word[x] == '\'')
        {
          cout << "'";

          continue;
        }

          }


      cout << endl;
      cout << endl;

      cout << "Would you like to enter another word (Y/N)? " << endl;
      cin >> yesno;
      yesno = toupper(yesno);
      cin.ignore();
      cout << endl; 
      cout << endl;
    }
  return 0;
}
