# EMA Hourly Continuation — DCR/USDT P26_50

**Symbol:** DCR/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1007 |
| net_profit_factor | 0.4142 |
| net_win_rate | 0.4161 |
| gross_profit_factor | 0.8223 |
| gross_win_rate | 0.4399 |
| sharpe_ratio | -9.0420 |
| sortino_ratio | -4.0606 |
| max_drawdown | 0.9940 |
| cagr | -0.8663 |
| net_avg_win | 16.7723 |
| net_avg_loss | -28.8523 |
| avg_hold_time_bars | 3.9752 |
| exposure | 0.1811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
