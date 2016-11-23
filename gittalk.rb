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

  def install
    system "make", "build" # if this fails, try separate make/make install steps
    system "make", "install"
  end

  test do
    system "gittalk"
  end
end
