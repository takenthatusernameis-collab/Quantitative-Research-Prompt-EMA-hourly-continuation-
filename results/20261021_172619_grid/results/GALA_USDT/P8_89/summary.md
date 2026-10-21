# EMA Hourly Continuation — GALA/USDT P8_89

**Symbol:** GALA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.7857 |
| net_win_rate | 0.4857 |
| gross_profit_factor | 0.9385 |
| gross_win_rate | 0.4857 |
| sharpe_ratio | -1.5531 |
| sortino_ratio | -0.4716 |
| max_drawdown | 0.4448 |
| cagr | -0.1962 |
| net_avg_win | 70.3536 |
| net_avg_loss | -84.5441 |
| avg_hold_time_bars | 31.9779 |
| exposure | 0.6585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
