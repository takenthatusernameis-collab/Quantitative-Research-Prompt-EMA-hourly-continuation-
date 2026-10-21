# EMA Hourly Continuation — ALGO/USDT P20_34

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.7983 |
| net_win_rate | 0.5343 |
| gross_profit_factor | 1.1344 |
| gross_win_rate | 0.5343 |
| sharpe_ratio | -1.1226 |
| sortino_ratio | -0.2704 |
| max_drawdown | 0.3218 |
| cagr | -0.1169 |
| net_avg_win | 71.6953 |
| net_avg_loss | -103.0403 |
| avg_hold_time_bars | 5.0939 |
| exposure | 0.0641 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
