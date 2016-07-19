# MaterialDesignIcons-C#-Consts
This C# class allows you to use [MaterialDesignIcons](https://github.com/Templarian/MaterialDesign)
project directly from your C# code: benefit from autocomplete and avoid typos.

![MaterialDesignIcons-CSharp-Consts](doc/screenshot.gif)

## How to use this
Copy [`generated/MaterialDesignIcons.cs`](https://raw.githubusercontent.com/chteuchteu/MaterialDesignIcons-CSharp-Consts/master/generated/MaterialDesignIcons.cs)
into your project, customize its namespace (`MyProject.Helpers`) and start using it!

## How to update `MaterialDesignIcons.cs` file

> Note: you usually don't want to do that, except if some icons are missing from the generated file.

The `generate.py` script generates `MaterialDesignIcons.cs` from MaterialDesignIcons input file:

    public const string AccessPoint = "mdi-access-point";
    public const string AccessPointNetwork = "mdi-access-point-network";
    public const string Account = "mdi-account";
    public const string AccountAlert = "mdi-account-alert";

1. Run `python generate.py`: [_variables.scss](https://raw.githubusercontent.com/Templarian/MaterialDesign-Webfont/master/scss/_variables.scss)
will be downloaded and parsed from MaterialDesignIcon's repository to update `MaterialDesignIcons.cs`.
2. Enjoy `MaterialDesignIcons.cs`!
