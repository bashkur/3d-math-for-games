from vector import *

if __name__ == "__main__":
    v = Vector(0, 0, 0, 0, 0)
    print(v)                                    # <Vector5: 0.0, 0.0, 0.0, 0.0, 0.0>
    w = Vector(1.2, "7", 5)
    # q = Vector(1.2, "abc", 5)                # Should raise an exception
    print(w)                                    # <Vector3: 1.2, 7.0, 5.0>
    z = w.copy()
    z[0] = 9.9
    z[-1] = "6"
    # z["abc"] = 9.9					 	    # Should raise an exception
    print(z)                                    # <Vector3: 9.9, 7.0, 6.0>
    print(w)                                    # <Vector3: 1.2, 7.0, 5.0>
    print(z == w)                               # False    [same as print(z.__eq__(w))]
    print(z == Vector(9.9, "7", 6))            # True
    print(z == 5)                               # False
    print(z[0])                                 # 9.9
    print(len(v))                               # 5
    print(w.i)          	                    # (1, 7, 5)

    w = Vector2(5, "3")
    print(w.__class__)                          # <class '__main__.Vector2'>
    k = Vector2(-1.4, 2)
    print(w.x)                                  # 5.0
    print(w.y)                                  # 3.0
    w.x = 6
    w.y = 4
    print(w)                                    # <Vector2: 6.0, 4.0>
    print(w.radians)                            # 0.5880026035475675
    print(w.degrees)                            # 33.690067525979785
    print(k.radians)                            # 2.181522291184105

    q = Vector3(9, 0, -2)
    q.z += 5
    print(q)                                    # <Vector3: 9.0, 0.0, 3.0>

    print(polar_to_vector2(1.459, 10.0))        # <Vector2: 1.1156359273295111, 9.937572967161127>