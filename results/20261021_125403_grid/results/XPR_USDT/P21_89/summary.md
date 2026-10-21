# EMA Hourly Continuation — XPR/USDT P21_89

**Symbol:** XPR/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.7504 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9528 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -1.8834 |
| sortino_ratio | -0.5288 |
| max_drawdown | 0.4890 |
| cagr | -0.2161 |
| net_avg_win | 73.1649 |
| net_avg_loss | -92.1090 |
| avg_hold_time_bars | 17.0310 |
| exposure | 0.2996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
