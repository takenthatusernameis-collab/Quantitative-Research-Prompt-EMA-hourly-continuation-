# EMA Hourly Continuation — POPCAT/USDT P20_144

**Symbol:** POPCAT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.6598 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.8467 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -2.8342 |
| sortino_ratio | -0.8628 |
| max_drawdown | 0.5948 |
| cagr | -0.3353 |
| net_avg_win | 61.1321 |
| net_avg_loss | -79.0509 |
| avg_hold_time_bars | 27.0495 |
| exposure | 0.5773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
