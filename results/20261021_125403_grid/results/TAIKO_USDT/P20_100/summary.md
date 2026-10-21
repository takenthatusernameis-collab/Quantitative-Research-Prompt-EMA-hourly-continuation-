# EMA Hourly Continuation — TAIKO/USDT P20_100

**Symbol:** TAIKO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.7946 |
| net_win_rate | 0.5079 |
| gross_profit_factor | 1.0148 |
| gross_win_rate | 0.5079 |
| sharpe_ratio | -1.5245 |
| sortino_ratio | -0.4731 |
| max_drawdown | 0.4820 |
| cagr | -0.1964 |
| net_avg_win | 69.6741 |
| net_avg_loss | -90.4969 |
| avg_hold_time_bars | 19.6230 |
| exposure | 0.4176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
