# EMA Hourly Continuation — CTC/USDT P12_50

**Symbol:** CTC/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1077 |
| net_profit_factor | 0.5248 |
| net_win_rate | 0.4596 |
| gross_profit_factor | 0.9915 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -7.0104 |
| sortino_ratio | -3.2309 |
| max_drawdown | 0.9829 |
| cagr | -0.7967 |
| net_avg_win | 21.9001 |
| net_avg_loss | -35.4939 |
| avg_hold_time_bars | 7.6667 |
| exposure | 0.3753 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
