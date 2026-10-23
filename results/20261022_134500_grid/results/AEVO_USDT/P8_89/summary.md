# EMA Hourly Continuation — AEVO/USDT P8_89

**Symbol:** AEVO/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.6728 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.9437 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -3.5453 |
| sortino_ratio | -1.2395 |
| max_drawdown | 0.7907 |
| cagr | -0.4494 |
| net_avg_win | 54.0570 |
| net_avg_loss | -71.6302 |
| avg_hold_time_bars | 24.5255 |
| exposure | 0.6970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
