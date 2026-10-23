# EMA Hourly Continuation — ORDI/USDT P100_144

**Symbol:** ORDI/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 535 |
| net_profit_factor | 0.4713 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.8062 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -5.1037 |
| sortino_ratio | -1.6626 |
| max_drawdown | 0.8716 |
| cagr | -0.5564 |
| net_avg_win | 32.7285 |
| net_avg_loss | -55.2270 |
| avg_hold_time_bars | 3.7290 |
| exposure | 0.0907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
