# EMA Hourly Continuation — UNI/USDT P34_89

**Symbol:** UNI/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.5777 |
| net_win_rate | 0.4792 |
| gross_profit_factor | 0.9414 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -4.5278 |
| sortino_ratio | -1.6532 |
| max_drawdown | 0.8705 |
| cagr | -0.5502 |
| net_avg_win | 36.6565 |
| net_avg_loss | -58.3923 |
| avg_hold_time_bars | 7.9852 |
| exposure | 0.2446 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
