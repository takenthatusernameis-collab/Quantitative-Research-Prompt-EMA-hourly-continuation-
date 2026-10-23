# EMA Hourly Continuation — PUFFER/USDT P8_21

**Symbol:** PUFFER/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1154 |
| net_profit_factor | 0.5287 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 0.8987 |
| gross_win_rate | 0.4497 |
| sharpe_ratio | -8.8277 |
| sortino_ratio | -4.6824 |
| max_drawdown | 0.9910 |
| cagr | -0.9018 |
| net_avg_win | 21.7921 |
| net_avg_loss | -32.6417 |
| avg_hold_time_bars | 4.0815 |
| exposure | 0.2665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
