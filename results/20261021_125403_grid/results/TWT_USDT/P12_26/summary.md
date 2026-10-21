# EMA Hourly Continuation — TWT/USDT P12_26

**Symbol:** TWT/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 558 |
| net_profit_factor | 0.5497 |
| net_win_rate | 0.4713 |
| gross_profit_factor | 0.8601 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -4.1613 |
| sortino_ratio | -1.4122 |
| max_drawdown | 0.8068 |
| cagr | -0.4767 |
| net_avg_win | 37.2816 |
| net_avg_loss | -60.4680 |
| avg_hold_time_bars | 5.1183 |
| exposure | 0.1298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
