def Inverse(mx):
    if Determinant(mx) == 0:
        return None  # The inverse does not exist in this case
    else:
        return Division(Adjoint(mx), Determinant(mx))  # By definition