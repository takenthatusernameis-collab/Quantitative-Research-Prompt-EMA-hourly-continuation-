# EMA Hourly Continuation — GLM/USDT P8_20

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 776 |
| net_profit_factor | 0.6463 |
| net_win_rate | 0.4961 |
| gross_profit_factor | 1.0028 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -4.2410 |
| sortino_ratio | -1.6996 |
| max_drawdown | 0.8605 |
| cagr | -0.5401 |
| net_avg_win | 40.7079 |
| net_avg_loss | -62.0229 |
| avg_hold_time_bars | 5.2126 |
| exposure | 0.1839 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
