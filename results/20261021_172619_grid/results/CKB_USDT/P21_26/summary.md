# EMA Hourly Continuation — CKB/USDT P21_26

**Symbol:** CKB/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 187 |
| net_profit_factor | 0.4918 |
| net_win_rate | 0.4118 |
| gross_profit_factor | 0.7168 |
| gross_win_rate | 0.4118 |
| sharpe_ratio | -3.1356 |
| sortino_ratio | -0.6119 |
| max_drawdown | 0.5292 |
| cagr | -0.2462 |
| net_avg_win | 63.8721 |
| net_avg_loss | -90.9067 |
| avg_hold_time_bars | 4.8770 |
| exposure | 0.0415 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
