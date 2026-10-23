# EMA Hourly Continuation — FIDA/USDT P55_144

**Symbol:** FIDA/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.5394 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8218 |
| gross_win_rate | 0.4528 |
| sharpe_ratio | -4.1113 |
| sortino_ratio | -1.3072 |
| max_drawdown | 0.7903 |
| cagr | -0.4602 |
| net_avg_win | 40.5219 |
| net_avg_loss | -61.1692 |
| avg_hold_time_bars | 11.9567 |
| exposure | 0.2749 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
