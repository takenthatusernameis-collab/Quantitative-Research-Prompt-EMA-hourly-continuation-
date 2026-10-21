# EMA Hourly Continuation — SUN/USDT P8_26

**Symbol:** SUN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 756 |
| net_profit_factor | 0.4868 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9141 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -6.5549 |
| sortino_ratio | -2.5793 |
| max_drawdown | 0.9557 |
| cagr | -0.7084 |
| net_avg_win | 25.3806 |
| net_avg_loss | -46.6522 |
| avg_hold_time_bars | 8.3360 |
| exposure | 0.2852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
