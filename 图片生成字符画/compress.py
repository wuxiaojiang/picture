#--------------------------------------------------------------------------------
#          pppppp                                                  pppp          
#      pppppppppppppp              pp                          pppppppppppp      
#      pppppppppppppppp                                      pppppppppppppppp    
#    pppppppppppppppppp                                    pppppppppppppppppppp  
#    pppppppppppppppp                                        pppppppppppppppppp  
#  pppppppppppppppppp                                          pppppppppppppppp  
#  pppppppppppppppp                                              pppppppppppppp  
#    pppppppppppp                                                  pppppppppppp  
#    pppppppppppp                                                  pppppppppppp  
#    pppppppppp                    pppppp          pppp              pppppppp    
#      pppppppp                      pppp                            pppppppp    
#        pppp                pppppppppppp        pppp                  pppp      
#          pp              pppppppppppppp      pp  pppppp              pp        
#                                                                                
#                                                                                
#                                  pp                                            
#                                pp                                              
#                                        pppppp                                  
#      pp                                                                        
#    pppp                          pppppppppppppp                        pp      
#  pppppp                        pppppppp    pppp                        pppp    
#pppppppp                          pppp    pppppp                        pppp    
#pppppppp                                                                pppppp  
#pppppppp                          pppp                                  pppppppp
#pppppppppp                                                            pppppppppp
#pppppppppppp                                                          pppppppppp
#pppppppppppppp                                                      pppppppppppp
#pppppppppppppppp                                                  pppppppppppppp
#pppppppppppppppppppp                                          pppppppppppppppppp
#pppppppppppppppppppppppp                                  pppppppppppppppppppppp
#pppppppppppppppppppppppppppppp                  pppppppppppppppppppppppppppppppp
#pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
#pppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppppp
#---------------------------------------------------------------------------------
from PIL import Image
im = Image.open('doubi.png')
w,h = im.size
im.thumbnail((50, 50))
im.save('hello.png')
