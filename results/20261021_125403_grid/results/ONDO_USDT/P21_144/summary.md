# EMA Hourly Continuation — ONDO/USDT P21_144

**Symbol:** ONDO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.9242 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.0842 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -0.4624 |
| sortino_ratio | -0.1279 |
| max_drawdown | 0.3566 |
| cagr | -0.0613 |
| net_avg_win | 93.3479 |
| net_avg_loss | -109.5583 |
| avg_hold_time_bars | 27.3388 |
| exposure | 0.4585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
