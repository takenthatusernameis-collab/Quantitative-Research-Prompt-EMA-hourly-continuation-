# EMA Hourly Continuation — API3/USDT P12_26

**Symbol:** API3/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 512 |
| net_profit_factor | 0.6344 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8707 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -3.5307 |
| sortino_ratio | -1.1400 |
| max_drawdown | 0.7360 |
| cagr | -0.4073 |
| net_avg_win | 53.9812 |
| net_avg_loss | -72.1915 |
| avg_hold_time_bars | 7.2070 |
| exposure | 0.1677 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
