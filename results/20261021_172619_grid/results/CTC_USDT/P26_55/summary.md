# EMA Hourly Continuation — CTC/USDT P26_55

**Symbol:** CTC/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.7184 |
| net_win_rate | 0.5105 |
| gross_profit_factor | 1.0414 |
| gross_win_rate | 0.5105 |
| sharpe_ratio | -2.2205 |
| sortino_ratio | -0.6952 |
| max_drawdown | 0.5820 |
| cagr | -0.2729 |
| net_avg_win | 58.0590 |
| net_avg_loss | -84.3038 |
| avg_hold_time_bars | 7.7321 |
| exposure | 0.1666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
