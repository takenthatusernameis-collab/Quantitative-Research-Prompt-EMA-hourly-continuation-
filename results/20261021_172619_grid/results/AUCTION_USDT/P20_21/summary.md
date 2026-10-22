# EMA Hourly Continuation — AUCTION/USDT P20_21

**Symbol:** AUCTION/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 315 |
| net_profit_factor | 0.4430 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.7190 |
| gross_win_rate | 0.4032 |
| sharpe_ratio | -5.0024 |
| sortino_ratio | -1.2714 |
| max_drawdown | 0.7870 |
| cagr | -0.4545 |
| net_avg_win | 49.4407 |
| net_avg_loss | -74.3977 |
| avg_hold_time_bars | 5.4794 |
| exposure | 0.0781 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
