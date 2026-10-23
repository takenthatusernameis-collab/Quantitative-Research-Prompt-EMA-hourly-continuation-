# EMA Hourly Continuation — T/USDT P26_55

**Symbol:** T/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 741 |
| net_profit_factor | 0.4517 |
| net_win_rate | 0.4426 |
| gross_profit_factor | 0.8361 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -6.8693 |
| sortino_ratio | -2.6129 |
| max_drawdown | 0.9634 |
| cagr | -0.7306 |
| net_avg_win | 24.1953 |
| net_avg_loss | -42.5434 |
| avg_hold_time_bars | 6.3954 |
| exposure | 0.2145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
