# EMA Hourly Continuation — CSPR/USDT P12_100

**Symbol:** CSPR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.6978 |
| net_win_rate | 0.4597 |
| gross_profit_factor | 0.8572 |
| gross_win_rate | 0.4597 |
| sharpe_ratio | -2.6370 |
| sortino_ratio | -0.8644 |
| max_drawdown | 0.6415 |
| cagr | -0.3285 |
| net_avg_win | 59.5696 |
| net_avg_loss | -72.6256 |
| avg_hold_time_bars | 20.2777 |
| exposure | 0.4913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
