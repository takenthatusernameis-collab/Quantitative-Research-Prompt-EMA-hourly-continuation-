# EMA Hourly Continuation — PROM/USDT P12_144

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6064 |
| net_win_rate | 0.4449 |
| gross_profit_factor | 0.7907 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -3.2436 |
| sortino_ratio | -0.9950 |
| max_drawdown | 0.6958 |
| cagr | -0.3706 |
| net_avg_win | 50.4377 |
| net_avg_loss | -66.6643 |
| avg_hold_time_bars | 27.6208 |
| exposure | 0.5926 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
