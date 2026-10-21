# EMA Hourly Continuation — ARKM/USDT P20_21

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 140 |
| net_profit_factor | 0.6439 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.8800 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -1.5854 |
| sortino_ratio | -0.2681 |
| max_drawdown | 0.2690 |
| cagr | -0.1150 |
| net_avg_win | 72.3564 |
| net_avg_loss | -100.2272 |
| avg_hold_time_bars | 4.2643 |
| exposure | 0.0271 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
