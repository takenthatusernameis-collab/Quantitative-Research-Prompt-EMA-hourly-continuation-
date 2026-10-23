# EMA Hourly Continuation — QI/USDT P12_26

**Symbol:** QI/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1198 |
| net_profit_factor | 0.3699 |
| net_win_rate | 0.4149 |
| gross_profit_factor | 0.7563 |
| gross_win_rate | 0.4357 |
| sharpe_ratio | -10.1874 |
| sortino_ratio | -4.9978 |
| max_drawdown | 0.9980 |
| cagr | -0.9152 |
| net_avg_win | 11.7893 |
| net_avg_loss | -22.5956 |
| avg_hold_time_bars | 3.9098 |
| exposure | 0.2120 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
