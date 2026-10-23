# EMA Hourly Continuation — ILV/USDT P34_55

**Symbol:** ILV/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 902 |
| net_profit_factor | 0.4890 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.9573 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -7.7772 |
| sortino_ratio | -3.2955 |
| max_drawdown | 0.9851 |
| cagr | -0.8076 |
| net_avg_win | 23.0799 |
| net_avg_loss | -38.9824 |
| avg_hold_time_bars | 3.2262 |
| exposure | 0.1323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
