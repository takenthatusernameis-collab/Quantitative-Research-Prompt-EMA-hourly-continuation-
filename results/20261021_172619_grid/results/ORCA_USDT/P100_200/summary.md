# EMA Hourly Continuation — ORCA/USDT P100_200

**Symbol:** ORCA/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 0.5961 |
| net_win_rate | 0.4510 |
| gross_profit_factor | 0.7862 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -2.5295 |
| sortino_ratio | -0.6066 |
| max_drawdown | 0.5478 |
| cagr | -0.2451 |
| net_avg_win | 57.9409 |
| net_avg_loss | -79.8635 |
| avg_hold_time_bars | 11.5350 |
| exposure | 0.1500 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
