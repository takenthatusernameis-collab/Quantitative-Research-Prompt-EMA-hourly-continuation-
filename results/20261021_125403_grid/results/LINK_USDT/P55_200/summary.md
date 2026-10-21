# EMA Hourly Continuation — LINK/USDT P55_200

**Symbol:** LINK/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.9002 |
| net_win_rate | 0.5379 |
| gross_profit_factor | 1.1382 |
| gross_win_rate | 0.5379 |
| sharpe_ratio | -0.4809 |
| sortino_ratio | -0.1156 |
| max_drawdown | 0.2350 |
| cagr | -0.0542 |
| net_avg_win | 79.0321 |
| net_avg_loss | -102.1928 |
| avg_hold_time_bars | 25.7256 |
| exposure | 0.3239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
