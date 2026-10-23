# EMA Hourly Continuation — DUSK/USDT P8_55

**Symbol:** DUSK/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.6671 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.9928 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -5.5412 |
| sortino_ratio | -2.4772 |
| max_drawdown | 0.9524 |
| cagr | -0.6947 |
| net_avg_win | 41.5317 |
| net_avg_loss | -51.2831 |
| avg_hold_time_bars | 11.1499 |
| exposure | 0.5139 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
