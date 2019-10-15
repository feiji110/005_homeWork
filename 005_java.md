````java
import java.io.FileInputStream;

import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;

public class Excel {
	
	public static void main(String args[]) {
		double[] arr = new double(54);
		//4.2读取所有学生成绩单中期末成绩 （40分）	5
	
//		arr = readExcel("C:\\tmp\Grade.xls");

		//4.3 计算所有学生成绩分布情况（20分）	5
		//4.4 生成成绩分析Excel文档（40分）	6

	}
	public static void readExcel(String path) {	
		try {
		// 获得Excel文件输入流
		FileInputStream  inputStream = new FileInputStream(path);
		// 创建对Excel工作簿文件的引用
		HSSFWorkbook workbook = new HSSFWorkbook(inputStream);
        // 创建对工作表的引用。		        // 得到Excel工作簿的第一页，即excel工作表对象
		// 在Excel文档中，第一张工作表的索引是0
		HSSFSheet sheet = workbook.getSheetAt(0);
		//循环读取表格数据 
		double[] arr = new double(54);
	    for (int j = 0; j < arr.length; j++) {
	    	// 创建工作表中一行，索引从0开始
	    	HSSFRow row1 = sheet.createRow(j+1);
			//得到某一行的第一个单元格，单元格的索引也是从0开始
			HSSFCell cell = row.getCell(6);
			//如果要获得数字类型的值可以使用getNumericCellValue()方法     
			arr[j] = cell.getNumericCellValue();
	    }	       
	    in.close();// 关闭文件输入流
		catch (Exception e) {//上面程序正确时，不会执行此处代码
			 System.out.println("出错了！");
         	 e.printStackTrace();
		}}    
		    return arr;
	}

	
//     public void static analysis(double[] arr) {
//    	 	
//     }
//		
	
}


public class TestStudent {

	
	
}
````
