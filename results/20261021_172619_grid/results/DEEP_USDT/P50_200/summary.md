# EMA Hourly Continuation — DEEP/USDT P50_200

**Symbol:** DEEP/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 206 |
| net_profit_factor | 0.9495 |
| net_win_rate | 0.5243 |
| gross_profit_factor | 1.0881 |
| gross_win_rate | 0.5243 |
| sharpe_ratio | -0.1952 |
| sortino_ratio | -0.0450 |
| max_drawdown | 0.1628 |
| cagr | -0.0245 |
| net_avg_win | 84.9103 |
| net_avg_loss | -98.5493 |
| avg_hold_time_bars | 36.5631 |
| exposure | 0.4265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
