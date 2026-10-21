# EMA Hourly Continuation — ORDI/USDT P12_144

**Symbol:** ORDI/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7037 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.8211 |
| gross_win_rate | 0.4439 |
| sharpe_ratio | -2.3125 |
| sortino_ratio | -0.6323 |
| max_drawdown | 0.5305 |
| cagr | -0.2525 |
| net_avg_win | 74.1703 |
| net_avg_loss | -84.1224 |
| avg_hold_time_bars | 39.3048 |
| exposure | 0.6682 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
