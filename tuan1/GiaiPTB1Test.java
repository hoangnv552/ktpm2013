import static org.junit.Assert.assertEquals;

import org.junit.Test;


public class GiaiPTB1Test {

	@Test
	public void test1() {
		GiaiPTB1 gpt = new GiaiPTB1();
		int kq=gpt.GiaiPTB1(1,1);
		assertEquals(kq,-1);
	}
	@Test
	public void test2() {
		GiaiPTB1 gpt = new GiaiPTB1();
		int kq=gpt.GiaiPTB1(10,-90);
		assertEquals(kq,9);
	}

}
