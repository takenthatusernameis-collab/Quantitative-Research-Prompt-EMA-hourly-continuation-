# EMA Hourly Continuation — RUNE/USDT P50_144

**Symbol:** RUNE/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 446 |
| net_profit_factor | 0.6587 |
| net_win_rate | 0.5157 |
| gross_profit_factor | 0.9973 |
| gross_win_rate | 0.5202 |
| sharpe_ratio | -2.2419 |
| sortino_ratio | -0.6684 |
| max_drawdown | 0.6126 |
| cagr | -0.2728 |
| net_avg_win | 46.2086 |
| net_avg_loss | -74.6996 |
| avg_hold_time_bars | 15.3946 |
| exposure | 0.3121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
