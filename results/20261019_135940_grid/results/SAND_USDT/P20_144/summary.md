# EMA Hourly Continuation — SAND/USDT P20_144

**Symbol:** SAND/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.6327 |
| net_win_rate | 0.4607 |
| gross_profit_factor | 0.9234 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -3.6587 |
| sortino_ratio | -1.1326 |
| max_drawdown | 0.7502 |
| cagr | -0.4157 |
| net_avg_win | 57.2020 |
| net_avg_loss | -77.2489 |
| avg_hold_time_bars | 24.1798 |
| exposure | 0.5320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
