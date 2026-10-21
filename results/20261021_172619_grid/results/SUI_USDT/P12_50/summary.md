# EMA Hourly Continuation — SUI/USDT P12_50

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.7978 |
| net_win_rate | 0.4939 |
| gross_profit_factor | 0.9927 |
| gross_win_rate | 0.4939 |
| sharpe_ratio | -1.9041 |
| sortino_ratio | -0.6520 |
| max_drawdown | 0.5866 |
| cagr | -0.2598 |
| net_avg_win | 73.9179 |
| net_avg_loss | -90.4170 |
| avg_hold_time_bars | 11.1431 |
| exposure | 0.2902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
