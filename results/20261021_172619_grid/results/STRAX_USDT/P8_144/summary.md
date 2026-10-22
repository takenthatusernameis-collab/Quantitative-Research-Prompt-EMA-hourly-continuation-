# EMA Hourly Continuation — STRAX/USDT P8_144

**Symbol:** STRAX/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.6669 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.8368 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -3.3503 |
| sortino_ratio | -1.1163 |
| max_drawdown | 0.7251 |
| cagr | -0.4022 |
| net_avg_win | 59.0938 |
| net_avg_loss | -71.1802 |
| avg_hold_time_bars | 24.9927 |
| exposure | 0.6285 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
