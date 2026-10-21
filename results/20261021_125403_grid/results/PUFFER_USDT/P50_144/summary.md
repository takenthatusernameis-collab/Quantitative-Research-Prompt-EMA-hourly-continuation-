# EMA Hourly Continuation — PUFFER/USDT P50_144

**Symbol:** PUFFER/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.7657 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9255 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -1.5743 |
| sortino_ratio | -0.4385 |
| max_drawdown | 0.3639 |
| cagr | -0.1834 |
| net_avg_win | 74.0951 |
| net_avg_loss | -90.6429 |
| avg_hold_time_bars | 15.4379 |
| exposure | 0.2673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
