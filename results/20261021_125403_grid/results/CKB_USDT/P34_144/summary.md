# EMA Hourly Continuation — CKB/USDT P34_144

**Symbol:** CKB/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7894 |
| net_win_rate | 0.4987 |
| gross_profit_factor | 0.9879 |
| gross_win_rate | 0.4987 |
| sharpe_ratio | -1.4340 |
| sortino_ratio | -0.3962 |
| max_drawdown | 0.3810 |
| cagr | -0.1678 |
| net_avg_win | 74.4713 |
| net_avg_loss | -93.8370 |
| avg_hold_time_bars | 22.5094 |
| exposure | 0.3816 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
