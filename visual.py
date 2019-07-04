def print_tex(L,boxlength, filename):

          with open(filename, "w+") as file_object:

                  
                    
                    file_object.write('\documentclass{article}\n')
                    file_object.write('\n')
                    file_object.write('\\usepackage{tikz}\n')
                    file_object.write('\\usetikzlibrary{calc}\n')
                    file_object.write('\n'
                    '\\begin{document}\n')
                    
                    file_object.write('\\begin{figure}\n')
                    file_object.write('\t\\')
                    
                    file_object.write('tikzset{\n')
                    file_object.write('            tick/.style = {black, very thick}\n')
                    file_object.write('          }\n')
                    file_object.write('\n')
                    file_object.write('\n')
                    file_object.write('\n')
                    file_object.write('\\begin{tikzpicture}')
                    file_object.write('\n')
                    file_object.write('\n')
                    for i in range(len(L)):
                              for j in range(len(L[i])):
                                      file_object.write('\draw [ultra thick] ('+str(j*boxlength)+','+str(i*boxlength)+') rectangle ('+str((j+1)*boxlength)+','+str((i+1)*boxlength)+');\n')
                                      file_object.write('\\node at ($('+str(float(j*boxlength))+','+str(float(i*boxlength))+')+('+str(boxlength/2)+','+str(boxlength/2)+')$) {$'+str(L[i][j])+'$};\n')
                                      file_object.write('\n')
                    file_object.write('\n')
                    file_object.write('\n')
                    file_object.write('\n')
                    file_object.write('\end{tikzpicture}\n')
                    file_object.write('\end{figure}\n')
                    file_object.write('\end{document}')
                    file_object.close()
