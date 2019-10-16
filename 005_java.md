````java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.text.NumberFormat;
import java.util.Arrays;

import org.apache.poi.hssf.usermodel.HSSFCell;
import org.apache.poi.hssf.usermodel.HSSFRow;
import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;

public class Excel {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		readExcel();
	}
	public static void readExcel() {
		try {
			double[] arr =  new double [53];
				// 获得Excel文件输入流
				FileInputStream  in = new FileInputStream("C:\\tmp\\成绩单.xls");
		        // 创建对Excel工作簿文件的引用
		        HSSFWorkbook workbook = new HSSFWorkbook(in);
		        // 创建对工作表的引用。
		        // 得到Excel工作簿的第一页，即excel工作表对象
		        // 在Excel文档中，第一张工作表的索引是0
		        HSSFSheet sheet = workbook.getSheetAt(0);
		        
		        // 得到工作表中第j行的引用，第j行的索引是j
		      for (int j = 1; j <= arr.length; j++) {
		        	HSSFRow row = sheet.getRow(j);
		        	//得到某j行的第6个单元格，单元格的索引也是从0开始
		        	HSSFCell cell = row.getCell(6);
		        	//cell.getStringCellValue()就是取所在单元的字符串类型的值
		        	//如果要获得数字类型的值可以使用getNumericCellValue()方法
		        	arr[j-1] = cell.getNumericCellValue();
		    }
		      analysisExcel(arr);
		         in.close();// 关闭文件输入流
		         workbook.close();
		    } catch (Exception e) {//上面程序正确时，不会执行此处代码
		        System.out.println("出错了！");
		        e.printStackTrace();
		    }   
	}
	public static void analysisExcel( double[] arr) {
		double[] brr = new double [8];
		for (int i = 0; i < brr.length; i++) {
			brr[i] = 0;
		}
		for (int i = 0; i < arr.length; i++) {
	    	brr[0] += arr[i];  
			if(arr[i]<60) {
				brr[1]++;
			}
			if(arr[i] >= 60&&arr[i] < 70) {
				brr[2]++;
			}
			if(arr[i] >= 70&&arr[i] < 80) {
				brr[3]++;
			}
			if(arr[i] >= 80&&arr[i] < 90) {
				brr[4]++;
			}
			if(arr[i] >=90&&arr[i] <= 100 ) {
				brr[5]++;
			}
		}
		Arrays.sort(arr);
		brr[6] = arr[0];
		brr[7] = arr[52];
		writeExcel(brr);
	}
	public static void writeExcel(double[] crr) {
		try {
			// 获得Excel文件输入流
			FileInputStream in = new FileInputStream("C:\\tmp\\成绩分析.xls");
			// 创建excel工作簿对象
			HSSFWorkbook wb = new HSSFWorkbook(in);
			// 获得excel中第一个工作页对象，索引从0开始
			HSSFSheet sheet = wb.getSheetAt(0);
			// 创建工作表中一行，索引从0开始
			HSSFRow row1 = sheet.getRow(1);
//			// 创建工作表中单元格，索引从0开始
//			HSSFCell cell1_1 = row1.createCell(0);
//			// 设置单元格内容
//			cell1_1.setCellValue("成绩分析" );
			HSSFCell cell1_2 = row1.createCell(2);
		    cell1_2.setCellValue(crr[5]);
			
			HSSFCell cell1_3 = row1.createCell(3);
		    cell1_3.setCellValue(crr[4]);
		    
			HSSFCell cell1_4 = row1.createCell(4);
		    cell1_4.setCellValue(crr[3]);
		    
			HSSFCell cell1_5 = row1.createCell(5);
		    cell1_5.setCellValue(crr[2]);
		    
			HSSFCell cell1_6 = row1.createCell(6);
		    cell1_6.setCellValue(crr[1]);
		    
			HSSFRow row2 = sheet.getRow(2);
			NumberFormat s = NumberFormat.getPercentInstance();
			s.setMinimumFractionDigits(2);
			HSSFCell cell2_2 = row2.createCell(2);
		    cell2_2.setCellValue(""+s.format((double)crr[5]/53));
			
			HSSFCell cell2_3 = row2.createCell(3);
		    cell2_3.setCellValue(""+s.format((double)crr[4]/53));
		    
			HSSFCell cell2_4 = row2.createCell(4);
		    cell2_4.setCellValue(""+s.format((double)crr[3]/53));
		    
			HSSFCell cell2_5 = row2.createCell(5);
		    cell2_5.setCellValue(""+s.format((double)crr[2]/53));
		    
			HSSFCell cell2_6 = row2.createCell(6);
		    cell2_6.setCellValue(""+s.format((double)crr[1]/53));
		    
			HSSFRow row3 = sheet.getRow(3);
		    HSSFCell cell3_2 = row3.createCell(2);
		    cell3_2.setCellValue(""+(double)crr[0]/53);
		    
			HSSFCell cell3_4 = row3.createCell(4);
		    cell3_4.setCellValue(crr[7]);
		    
			HSSFCell cell3_6 = row3.createCell(6);
		    cell3_6.setCellValue(crr[6]);
		    
			// 获得Excel文件输出流
			FileOutputStream out = new FileOutputStream("C:\\tmp\\成绩分析.xls");
			// 输出excel
			wb.write(out);
			// 关闭文件输入、输出流
			in.close();
			out.close();
			wb.close();
		} catch (Exception e) {
			// 上面程序正确时，不会执行此处代码
			System.out.println("出错了！");
			e.printStackTrace();
		}
	}


}
