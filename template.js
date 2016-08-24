l = new Level("/Users/keisuke_ogaki/Documents/opentoonz/music/testras.0001.tif");
f_orig = l.getFrame(1);

builder = new ImageBuilder();
builder.add(f_orig, (new Transform).scale(2.0));
f = builder.image;
l.setFrame(2, f);

builder = new ImageBuilder();
builder.add(f_orig, (new Transform).scale(4.0));
f = builder.image;
l.setFrame(3, f);

builder = new ImageBuilder();
builder.add(f_orig, (new Transform).scale(6.0));
f = builder.image;
l.setFrame(4, f);

builder = new ImageBuilder();
builder.add(f_orig, (new Transform).scale(8.0));
f = builder.image;
l.setFrame(5, f);

l.save("/Users/keisuke_ogaki/Documents/opentoonz/music/testras2.0001.tif");
