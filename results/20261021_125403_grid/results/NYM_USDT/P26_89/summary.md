# EMA Hourly Continuation — NYM/USDT P26_89

**Symbol:** NYM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.5121 |
| net_win_rate | 0.4314 |
| gross_profit_factor | 0.7789 |
| gross_win_rate | 0.4400 |
| sharpe_ratio | -3.7167 |
| sortino_ratio | -0.9885 |
| max_drawdown | 0.6937 |
| cagr | -0.3681 |
| net_avg_win | 47.5640 |
| net_avg_loss | -70.4776 |
| avg_hold_time_bars | 19.7086 |
| exposure | 0.3135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
