from game import game

from solver import solver as so

if __name__ == "__main__":
    gm = game.game()
    #gm.new_game(16, 10)
    # gm.show_game()
    # ret=so.guess(gm.label_m[0],gm.n,[])
    # print so.ana(ret)




    ret = so.guess("13", 18, [])
    print so.ana(ret)
