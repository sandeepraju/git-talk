# Documentation: https://github.com/Homebrew/brew/blob/master/docs/Formula-Cookbook.md
#                http://www.rubydoc.info/github/Homebrew/brew/master/Formula
# PLEASE REMOVE ALL GENERATED COMMENTS BEFORE SUBMITTING YOUR PULL REQUEST!

class Gittalk < Formula
  depends_on "ffmpeg" => :run
  
  desc "338"
  homepage "https://github.com/sandeepraju/git-talk"
  url "https://github.com/sandeepraju/git-talk/archive/0.0.5a0.tar.gz"
  sha256 "407b927ef676504ed5cec610f71a82de2d02ed836fdd3fae814c6533bc84d650"
  version '0.9'

  # depends_on "cmake" => :build
#  depends_on :x11 # if your formula requires any X11/XQuartz components

  def install
    # ENV.deparallelize  # if your formula fails when building in parallel

    # Remove unrecognized options if warned by configure
#    system "./configure", "--disable-debug",
#                          "--disable-dependency-tracking",
#                          "--disable-silent-rules",
#                          "--prefix=#{prefix}"
    # system "cmake", ".", *std_cmake_args
#    system "bash"
    system "make", "build" # if this fails, try separate make/make install steps
    system "make", "install"
  end

  test do
    # `test do` will create, run in and delete a temporary directory.
    #
    # This test will fail and we won't accept that! It's enough to just replace
    # "false" with the main program this formula installs, but it'd be nice if you
    # were more thorough. Run the test with `brew test gittalk`. Options passed
    # to `brew install` such as `--HEAD` also need to be provided to `brew test`.
    #
    # The installed folder is not in the path, so use the entire path to any
    # executables being tested: `system "#{bin}/program", "do", "something"`.
    system "gittalk"
  end
end
