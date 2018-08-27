from .commands import Command


class AGSMainMagnet(Command):
    """AGS main magnet."""
    KEYWORD = 'AGSMM'


class AGSQuadrupole(Command):
    """AGS quadrupole."""
    KEYWORD = 'AGSQUAD'


class Aimant(Command):
    """Generation of dipole mid-plane 2-D map, polar frame."""
    KEYWORD = 'AIMANT'


class Bend(Command):
    """Bending magnet, Cartesian frame."""
    KEYWORD = 'BEND'


class Decapole(Command):
    """Decapole magnet."""
    KEYWORD = 'DECAPOLE'


class Dipole(Command):
    """Dipole magnet, polar frame."""
    KEYWORD = 'DIPOLE'


class DipoleM(Command):
    """Generation of dipole mid-plane 2-D map, polar frame."""
    KEYWORD = 'DIPOLE-M'

    PARAMETERS = {
        'NFACE': 3,
        'IC': 1,
        'IL': 1,
        'IAMAX': 1,
        'IRMAX': 1,
        'B0': 1,
        'N': 1,
        'B': 1,
        'G': 1,
        'AT': 1,
        'ACENT': 1,
        'RM': 1,
        'RMIN': 1,
        'RMAX': 1,
        'entrance_fb_lambda': 1,
        'entrance_fb_xi': 1,
        'entrance_fb_NC': 1,
        'entrance_fb_C1': 1,
        'entrance_fb_C2': 1,
        'entrance_fb_C3': 1,
        'entrance_fb_C4': 1,
        'entrance_fb_C5': 1,
        'entrance_fb_shift': 1,
        'omega_minus': 1,
        'theta': 1,
        'R1': 1,
        'U1': 1,
        'U2': 1,
        'R2': 1,

    }

    def __str__(s):
        c = f"""
        '{s.KEYWORD}' {s.LABEL1} {s.LABEL2}
        {s.NFACE} {s.IC} {s.IL}
        {s.IAMAX} {s.IRMAX}
        {s.B0} {s.N} {s.B} {s.G}
        {s.AT} {ACENT} {s.RM}
        {s.RMIN} {s.RMAX}
        {s.entrance_fb_lambda} {s.entrance_fb_xi}
        {s.entrance_fb_NC} {s.entrance_fb_C1} {s.entrance_fb_C2} {s.entrance_fb_C3} {s.entrance_fb_C4} {s.entrance_fb_C5} {s.entrance_fb_shift}
        
        """
        return c


class Dipoles(Command):
    """Dipole magnet N-tuple, polarframe."""
    KEYWORD = 'DIPOLES'


class Dodecapole(Command):
    """Dodecapole magnet."""
    KEYWORD = 'DODECAPO'


class Drift(Command):
    """Field free drift space."""
    KEYWORD = 'DRIFT'

    PARAMETERS = {
        'XL': 0.0
    }

    def __str__(s):
        return f"""
        '{s.KEYWORD}' {s.LABEL1} {s.LABEL2}
        {s.XL}
        """


class Emma(Command):
    """2-D Cartesian or cylindrical mesh field map for EMMA FFAG."""
    KEYWORD = 'EMMA'


class FFAG(Command):
    """FFAG magnet, N-tuple."""
    KEYWORD = 'FFAG'


class FFAGSpirale(Command):
    """Spiral FFAG magnet, N-tuple."""
    KEYWORD = 'FFAG-SPI'


class Multipole(Command):
    """Magnetic multipole."""
    KEYWORD = 'MULTIPOL'


class Octupole(Command):
    """Octupole magnet."""
    KEYWORD = 'OCTUPOLE'


class PS170(Command):
    """Simulation of a round shape dipole magnet."""
    KEYWORD = 'PS170'


class Quadisex(Command):
    """Sharp edge magnetic multipoles."""
    KEYWORD = 'QUADISEX'


class Quadrupole(Command):
    """Quadrupole magnet."""
    KEYWORD = 'QUADRUPO'

    PARAMETERS = {
        'IL': 2,
        'XL': 0,
        'R0': 0,
        'B0': 0,
        'XE': 0,
        'LAM_E': 0,
        'NCE': 0,
        'NCS': 0,
        'C0': 0,
        'C1': 0,
        'C2': 0,
        'C3': 0,
        'C4': 0,
        'C5': 0,
        'XS': 0,
        'LAM_S': 0,
        'XPAS': 0.1,
        'KPOS': 0,
        'XCE': 0,
        'YCE': 0,
        'ALE': 0,
    }

    def __str__(s):
        return f"""
        {super().__str__().rstrip()}
        {s.IL}
        {s.XL:.12e} {s.R0:.12e} {s.B0:.12e}
        {s.XE:.12e} {s.LAM_E:.12e}
        {s.NCE} {s.C0:.12e} {s.C1:.12e} {s.C2:.12e} {s.C3:.12e} {s.C4:.12e} {s.C5:.12e}
        {s.XS:.12e} {s.LAM_S:.12e}
        {s.NCS} {s.C0:.12e} {s.C1:.12e} {s.C2:.12e} {s.C3:.12e} {s.C4:.12e} {s.C5:.12e}
        {s.XPAS}
        {s.KPOS} {s.XCE:.12e} {s.YCE:.12e} {s.ALE:.12e}
        """


class SexQuad(Command):
    """Sharp edge magnetic multipole."""
    KEYWORD = 'SEXQUAD'


class Sextupole(Command):
    """Sextupole magnet."""
    KEYWORD = 'SEXTUPOL'


class Solenoid(Command):
    """Solenoid."""
    KEYWORD = 'SOLENOID'


class Undulator(Command):
    """Undulator magnet."""
    KEYWORD = 'UNDULATOR'


class Venus(Command):
    """Simulation of a rectangular shape dipole magnet."""
    KEYWORD = 'VENUS'
