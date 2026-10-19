# EMA Hourly Continuation — AERO/USDT P8_200

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.9155 |
| net_win_rate | 0.5359 |
| gross_profit_factor | 1.1517 |
| gross_win_rate | 0.5359 |
| sharpe_ratio | -0.4634 |
| sortino_ratio | -0.1146 |
| max_drawdown | 0.2726 |
| cagr | -0.0575 |
| net_avg_win | 91.3266 |
| net_avg_loss | -115.2141 |
| avg_hold_time_bars | 58.6209 |
| exposure | 0.8154 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
