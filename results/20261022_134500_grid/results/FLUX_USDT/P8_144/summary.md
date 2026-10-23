# EMA Hourly Continuation — FLUX/USDT P8_144

**Symbol:** FLUX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.7518 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 1.0199 |
| gross_win_rate | 0.5094 |
| sharpe_ratio | -1.7810 |
| sortino_ratio | -0.5514 |
| max_drawdown | 0.5057 |
| cagr | -0.2300 |
| net_avg_win | 60.7363 |
| net_avg_loss | -81.8083 |
| avg_hold_time_bars | 35.0419 |
| exposure | 0.7598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
