# EMA Hourly Continuation — ORDI/USDT P8_144

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.6690 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8889 |
| gross_win_rate | 0.4605 |
| sharpe_ratio | -2.9909 |
| sortino_ratio | -0.8911 |
| max_drawdown | 0.6644 |
| cagr | -0.3391 |
| net_avg_win | 64.3612 |
| net_avg_loss | -81.3783 |
| avg_hold_time_bars | 38.8555 |
| exposure | 0.7824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
