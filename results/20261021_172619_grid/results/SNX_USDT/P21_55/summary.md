# EMA Hourly Continuation — SNX/USDT P21_55

**Symbol:** SNX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.8104 |
| net_win_rate | 0.5166 |
| gross_profit_factor | 1.0651 |
| gross_win_rate | 0.5166 |
| sharpe_ratio | -1.4946 |
| sortino_ratio | -0.4852 |
| max_drawdown | 0.4818 |
| cagr | -0.2004 |
| net_avg_win | 69.8104 |
| net_avg_loss | -92.0706 |
| avg_hold_time_bars | 8.1213 |
| exposure | 0.1878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
