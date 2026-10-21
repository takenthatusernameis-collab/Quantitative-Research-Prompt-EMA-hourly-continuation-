# EMA Hourly Continuation — CKB/USDT P26_144

**Symbol:** CKB/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.8580 |
| net_win_rate | 0.5234 |
| gross_profit_factor | 1.0726 |
| gross_win_rate | 0.5234 |
| sharpe_ratio | -0.8052 |
| sortino_ratio | -0.2208 |
| max_drawdown | 0.3093 |
| cagr | -0.0991 |
| net_avg_win | 73.3035 |
| net_avg_loss | -93.8285 |
| avg_hold_time_bars | 29.2066 |
| exposure | 0.4819 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
