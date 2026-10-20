# EMA Hourly Continuation — ANKR/USDT P20_26

**Symbol:** ANKR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1242 |
| net_profit_factor | 0.1857 |
| net_win_rate | 0.3374 |
| gross_profit_factor | 0.5879 |
| gross_win_rate | 0.3913 |
| sharpe_ratio | -15.5625 |
| sortino_ratio | -8.0064 |
| max_drawdown | 1.0000 |
| cagr | -0.9861 |
| net_avg_win | 5.4410 |
| net_avg_loss | -14.9205 |
| avg_hold_time_bars | 2.5475 |
| exposure | 0.1438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
