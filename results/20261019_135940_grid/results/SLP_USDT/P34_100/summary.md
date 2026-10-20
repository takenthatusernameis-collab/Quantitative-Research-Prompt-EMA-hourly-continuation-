# EMA Hourly Continuation — SLP/USDT P34_100

**Symbol:** SLP/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 744 |
| net_profit_factor | 0.6234 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 1.0002 |
| gross_win_rate | 0.4825 |
| sharpe_ratio | -4.7985 |
| sortino_ratio | -1.8458 |
| max_drawdown | 0.8949 |
| cagr | -0.5877 |
| net_avg_win | 42.4232 |
| net_avg_loss | -59.8053 |
| avg_hold_time_bars | 8.4220 |
| exposure | 0.2848 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
