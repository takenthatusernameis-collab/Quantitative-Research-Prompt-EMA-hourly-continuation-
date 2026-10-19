# EMA Hourly Continuation — AERO/USDT P89_144

**Symbol:** AERO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.4840 |
| net_win_rate | 0.4399 |
| gross_profit_factor | 0.8633 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -4.6351 |
| sortino_ratio | -1.3281 |
| max_drawdown | 0.8090 |
| cagr | -0.4828 |
| net_avg_win | 41.4611 |
| net_avg_loss | -67.2862 |
| avg_hold_time_bars | 5.0889 |
| exposure | 0.0962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
