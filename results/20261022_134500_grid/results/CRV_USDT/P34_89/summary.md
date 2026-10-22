# EMA Hourly Continuation — CRV/USDT P34_89

**Symbol:** CRV/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.5876 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 0.9549 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -4.8491 |
| sortino_ratio | -1.8587 |
| max_drawdown | 0.9000 |
| cagr | -0.5909 |
| net_avg_win | 36.4982 |
| net_avg_loss | -55.0215 |
| avg_hold_time_bars | 6.6285 |
| exposure | 0.2239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
