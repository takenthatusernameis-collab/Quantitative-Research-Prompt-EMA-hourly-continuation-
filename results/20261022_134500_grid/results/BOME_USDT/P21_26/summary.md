# EMA Hourly Continuation — BOME/USDT P21_26

**Symbol:** BOME/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1145 |
| net_profit_factor | 0.2983 |
| net_win_rate | 0.3974 |
| gross_profit_factor | 0.7680 |
| gross_win_rate | 0.4279 |
| sharpe_ratio | -11.8918 |
| sortino_ratio | -5.7575 |
| max_drawdown | 0.9994 |
| cagr | -0.9486 |
| net_avg_win | 9.3389 |
| net_avg_loss | -20.6426 |
| avg_hold_time_bars | 1.8603 |
| exposure | 0.0968 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
