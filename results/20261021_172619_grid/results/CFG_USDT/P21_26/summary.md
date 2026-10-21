# EMA Hourly Continuation — CFG/USDT P21_26

**Symbol:** CFG/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 150 |
| net_profit_factor | 0.6109 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8125 |
| gross_win_rate | 0.4533 |
| sharpe_ratio | -1.7776 |
| sortino_ratio | -0.3099 |
| max_drawdown | 0.3257 |
| cagr | -0.1324 |
| net_avg_win | 69.2843 |
| net_avg_loss | -94.0514 |
| avg_hold_time_bars | 35.5000 |
| exposure | 0.2420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
