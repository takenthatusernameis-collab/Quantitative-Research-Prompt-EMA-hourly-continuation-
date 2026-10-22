# EMA Hourly Continuation — ORBS/USDT P12_34

**Symbol:** ORBS/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 726 |
| net_profit_factor | 0.5340 |
| net_win_rate | 0.4187 |
| gross_profit_factor | 0.8043 |
| gross_win_rate | 0.4187 |
| sharpe_ratio | -6.3505 |
| sortino_ratio | -2.4436 |
| max_drawdown | 0.9430 |
| cagr | -0.6788 |
| net_avg_win | 35.5259 |
| net_avg_loss | -47.9213 |
| avg_hold_time_bars | 7.1515 |
| exposure | 0.2360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
