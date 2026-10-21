# EMA Hourly Continuation — BONK/USDT P50_100

**Symbol:** BONK/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.7854 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9583 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.3492 |
| sortino_ratio | -0.3485 |
| max_drawdown | 0.3881 |
| cagr | -0.1489 |
| net_avg_win | 75.7283 |
| net_avg_loss | -93.5102 |
| avg_hold_time_bars | 10.3945 |
| exposure | 0.1545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
