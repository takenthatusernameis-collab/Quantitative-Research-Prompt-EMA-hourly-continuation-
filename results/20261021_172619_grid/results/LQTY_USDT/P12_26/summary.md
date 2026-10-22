# EMA Hourly Continuation — LQTY/USDT P12_26

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.6827 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9594 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -2.9470 |
| sortino_ratio | -1.0421 |
| max_drawdown | 0.7104 |
| cagr | -0.3781 |
| net_avg_win | 49.9196 |
| net_avg_loss | -70.9940 |
| avg_hold_time_bars | 5.6907 |
| exposure | 0.1573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
