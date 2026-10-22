# EMA Hourly Continuation — FLOKI/USDT P8_55

**Symbol:** FLOKI/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1116 |
| net_profit_factor | 0.5732 |
| net_win_rate | 0.4525 |
| gross_profit_factor | 0.8759 |
| gross_win_rate | 0.4633 |
| sharpe_ratio | -6.6905 |
| sortino_ratio | -3.1215 |
| max_drawdown | 0.9788 |
| cagr | -0.7843 |
| net_avg_win | 26.0315 |
| net_avg_loss | -37.5342 |
| avg_hold_time_bars | 9.3853 |
| exposure | 0.4761 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
