# EMA Hourly Continuation — SLP/USDT P12_34

**Symbol:** SLP/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.6948 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9444 |
| gross_win_rate | 0.4773 |
| sharpe_ratio | -3.2652 |
| sortino_ratio | -1.1998 |
| max_drawdown | 0.7571 |
| cagr | -0.4228 |
| net_avg_win | 54.0790 |
| net_avg_loss | -71.0702 |
| avg_hold_time_bars | 6.8303 |
| exposure | 0.2049 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
