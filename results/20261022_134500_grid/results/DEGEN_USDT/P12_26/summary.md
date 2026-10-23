# EMA Hourly Continuation — DEGEN/USDT P12_26

**Symbol:** DEGEN/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1312 |
| net_profit_factor | 0.5610 |
| net_win_rate | 0.4398 |
| gross_profit_factor | 0.8825 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -8.2885 |
| sortino_ratio | -4.2359 |
| max_drawdown | 0.9947 |
| cagr | -0.8721 |
| net_avg_win | 22.0215 |
| net_avg_loss | -30.8146 |
| avg_hold_time_bars | 3.3399 |
| exposure | 0.1995 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
