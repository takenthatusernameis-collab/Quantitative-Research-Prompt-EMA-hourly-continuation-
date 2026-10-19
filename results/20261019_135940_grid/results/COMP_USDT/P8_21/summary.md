# EMA Hourly Continuation — COMP/USDT P8_21

**Symbol:** COMP/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1719 |
| net_profit_factor | 0.2354 |
| net_win_rate | 0.4049 |
| gross_profit_factor | 0.6104 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -13.5940 |
| sortino_ratio | -7.9939 |
| max_drawdown | 1.0000 |
| cagr | -0.9825 |
| net_avg_win | 4.4235 |
| net_avg_loss | -12.7843 |
| avg_hold_time_bars | 3.1140 |
| exposure | 0.2433 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
