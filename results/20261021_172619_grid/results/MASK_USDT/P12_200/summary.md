# EMA Hourly Continuation — MASK/USDT P12_200

**Symbol:** MASK/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.5912 |
| net_win_rate | 0.4377 |
| gross_profit_factor | 0.7564 |
| gross_win_rate | 0.4377 |
| sharpe_ratio | -2.8444 |
| sortino_ratio | -0.7312 |
| max_drawdown | 0.5910 |
| cagr | -0.2882 |
| net_avg_win | 57.6548 |
| net_avg_loss | -75.9145 |
| avg_hold_time_bars | 47.9696 |
| exposure | 0.7174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
