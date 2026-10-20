# EMA Hourly Continuation — XEC/USDT P8_89

**Symbol:** XEC/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 758 |
| net_profit_factor | 0.5870 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9527 |
| gross_win_rate | 0.4763 |
| sharpe_ratio | -4.9909 |
| sortino_ratio | -1.9203 |
| max_drawdown | 0.9110 |
| cagr | -0.6079 |
| net_avg_win | 36.1535 |
| net_avg_loss | -54.5473 |
| avg_hold_time_bars | 18.6530 |
| exposure | 0.6398 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
