from setuptools import setup

setup(
    name='diabetesReportReader',
    version='0.0.1',
    packages=['venv.lib.python3.7.site-packages.bs4', 'venv.lib.python3.7.site-packages.bs4.tests',
              'venv.lib.python3.7.site-packages.bs4.builder', 'venv.lib.python3.7.site-packages.cv2',
              'venv.lib.python3.7.site-packages.cv2.data', 'venv.lib.python3.7.site-packages.PIL',
              'venv.lib.python3.7.site-packages.rsa', 'venv.lib.python3.7.site-packages.enum',
              'venv.lib.python3.7.site-packages.grpc', 'venv.lib.python3.7.site-packages.grpc.beta',
              'venv.lib.python3.7.site-packages.grpc._cython', 'venv.lib.python3.7.site-packages.grpc._cython._cygrpc',
              'venv.lib.python3.7.site-packages.grpc.framework',
              'venv.lib.python3.7.site-packages.grpc.framework.common',
              'venv.lib.python3.7.site-packages.grpc.framework.foundation',
              'venv.lib.python3.7.site-packages.grpc.framework.interfaces',
              'venv.lib.python3.7.site-packages.grpc.framework.interfaces.base',
              'venv.lib.python3.7.site-packages.grpc.framework.interfaces.face',
              'venv.lib.python3.7.site-packages.grpc.experimental', 'venv.lib.python3.7.site-packages.idna',
              'venv.lib.python3.7.site-packages.click', 'venv.lib.python3.7.site-packages.flask',
              'venv.lib.python3.7.site-packages.flask.json', 'venv.lib.python3.7.site-packages.numpy',
              'venv.lib.python3.7.site-packages.numpy.ma', 'venv.lib.python3.7.site-packages.numpy.ma.tests',
              'venv.lib.python3.7.site-packages.numpy.doc', 'venv.lib.python3.7.site-packages.numpy.fft',
              'venv.lib.python3.7.site-packages.numpy.fft.tests', 'venv.lib.python3.7.site-packages.numpy.lib',
              'venv.lib.python3.7.site-packages.numpy.lib.tests', 'venv.lib.python3.7.site-packages.numpy.core',
              'venv.lib.python3.7.site-packages.numpy.core.tests', 'venv.lib.python3.7.site-packages.numpy.f2py',
              'venv.lib.python3.7.site-packages.numpy.f2py.tests', 'venv.lib.python3.7.site-packages.numpy.tests',
              'venv.lib.python3.7.site-packages.numpy.compat', 'venv.lib.python3.7.site-packages.numpy.compat.tests',
              'venv.lib.python3.7.site-packages.numpy.linalg', 'venv.lib.python3.7.site-packages.numpy.linalg.tests',
              'venv.lib.python3.7.site-packages.numpy.random', 'venv.lib.python3.7.site-packages.numpy.random.tests',
              'venv.lib.python3.7.site-packages.numpy.testing', 'venv.lib.python3.7.site-packages.numpy.testing.tests',
              'venv.lib.python3.7.site-packages.numpy.testing._private',
              'venv.lib.python3.7.site-packages.numpy.distutils',
              'venv.lib.python3.7.site-packages.numpy.distutils.tests',
              'venv.lib.python3.7.site-packages.numpy.distutils.command',
              'venv.lib.python3.7.site-packages.numpy.distutils.fcompiler',
              'venv.lib.python3.7.site-packages.numpy.matrixlib',
              'venv.lib.python3.7.site-packages.numpy.matrixlib.tests',
              'venv.lib.python3.7.site-packages.numpy.polynomial',
              'venv.lib.python3.7.site-packages.numpy.polynomial.tests', 'venv.lib.python3.7.site-packages.google.api',
              'venv.lib.python3.7.site-packages.google.rpc', 'venv.lib.python3.7.site-packages.google.auth',
              'venv.lib.python3.7.site-packages.google.auth.crypt',
              'venv.lib.python3.7.site-packages.google.auth.transport',
              'venv.lib.python3.7.site-packages.google.auth.compute_engine',
              'venv.lib.python3.7.site-packages.google.type', 'venv.lib.python3.7.site-packages.google.cloud.vision_v1',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1.gapic',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1.gapic.transports',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1.proto',
              'venv.lib.python3.7.site-packages.google.cloud.vision_helpers',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1p1beta1',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1p1beta1.gapic',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1p1beta1.gapic.transports',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1p1beta1.proto',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1p2beta1',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1p2beta1.gapic',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1p2beta1.gapic.transports',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1p2beta1.proto',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1p3beta1',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1p3beta1.gapic',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1p3beta1.gapic.transports',
              'venv.lib.python3.7.site-packages.google.cloud.vision_v1p3beta1.proto',
              'venv.lib.python3.7.site-packages.google.oauth2', 'venv.lib.python3.7.site-packages.google.logging.type',
              'venv.lib.python3.7.site-packages.google.api_core',
              'venv.lib.python3.7.site-packages.google.api_core.future',
              'venv.lib.python3.7.site-packages.google.api_core.gapic_v1',
              'venv.lib.python3.7.site-packages.google.api_core.operations_v1',
              'venv.lib.python3.7.site-packages.google.protobuf',
              'venv.lib.python3.7.site-packages.google.protobuf.util',
              'venv.lib.python3.7.site-packages.google.protobuf.pyext',
              'venv.lib.python3.7.site-packages.google.protobuf.compiler',
              'venv.lib.python3.7.site-packages.google.protobuf.internal',
              'venv.lib.python3.7.site-packages.google.protobuf.internal.import_test_package',
              'venv.lib.python3.7.site-packages.google.longrunning', 'venv.lib.python3.7.site-packages.pyasn1',
              'venv.lib.python3.7.site-packages.pyasn1.type', 'venv.lib.python3.7.site-packages.pyasn1.codec',
              'venv.lib.python3.7.site-packages.pyasn1.codec.ber', 'venv.lib.python3.7.site-packages.pyasn1.codec.cer',
              'venv.lib.python3.7.site-packages.pyasn1.codec.der',
              'venv.lib.python3.7.site-packages.pyasn1.codec.native', 'venv.lib.python3.7.site-packages.pyasn1.compat',
              'venv.lib.python3.7.site-packages.certifi', 'venv.lib.python3.7.site-packages.chardet',
              'venv.lib.python3.7.site-packages.chardet.cli', 'venv.lib.python3.7.site-packages.urllib3',
              'venv.lib.python3.7.site-packages.urllib3.util', 'venv.lib.python3.7.site-packages.urllib3.contrib',
              'venv.lib.python3.7.site-packages.urllib3.contrib._securetransport',
              'venv.lib.python3.7.site-packages.urllib3.packages',
              'venv.lib.python3.7.site-packages.urllib3.packages.backports',
              'venv.lib.python3.7.site-packages.urllib3.packages.ssl_match_hostname',
              'venv.lib.python3.7.site-packages.requests', 'venv.lib.python3.7.site-packages.cachetools',
              'venv.lib.python3.7.site-packages.concurrent', 'venv.lib.python3.7.site-packages.concurrent.futures',
              'venv.lib.python3.7.site-packages.pytesseract', 'venv.lib.python3.7.site-packages.googlesearch',
              'venv.lib.python3.7.site-packages.pyasn1_modules'],
    url='',
    license='',
    author='Senura Seneviratne',
    author_email='senuraa@msn.com',
    description=''
)
