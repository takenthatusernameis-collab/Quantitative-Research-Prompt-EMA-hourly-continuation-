# EMA Hourly Continuation — NYM/USDT P89_100

**Symbol:** NYM/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.0740 |
| net_win_rate | 0.2109 |
| gross_profit_factor | 0.3957 |
| gross_win_rate | 0.2976 |
| sharpe_ratio | -13.4543 |
| sortino_ratio | -4.9704 |
| max_drawdown | 0.9991 |
| cagr | -0.9388 |
| net_avg_win | 7.1326 |
| net_avg_loss | -25.7515 |
| avg_hold_time_bars | 3.4859 |
| exposure | 0.0841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
