# EMA Hourly Continuation — SUSHI/USDT P55_144

**Symbol:** SUSHI/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.7382 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9378 |
| gross_win_rate | 0.4842 |
| sharpe_ratio | -1.8590 |
| sortino_ratio | -0.5162 |
| max_drawdown | 0.5041 |
| cagr | -0.2122 |
| net_avg_win | 69.2895 |
| net_avg_loss | -88.1108 |
| avg_hold_time_bars | 13.3947 |
| exposure | 0.2303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
