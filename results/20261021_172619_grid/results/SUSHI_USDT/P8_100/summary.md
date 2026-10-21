# EMA Hourly Continuation — SUSHI/USDT P8_100

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.7007 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8562 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -2.5909 |
| sortino_ratio | -0.8195 |
| max_drawdown | 0.6342 |
| cagr | -0.3148 |
| net_avg_win | 62.8488 |
| net_avg_loss | -76.0700 |
| avg_hold_time_bars | 28.6052 |
| exposure | 0.6459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
