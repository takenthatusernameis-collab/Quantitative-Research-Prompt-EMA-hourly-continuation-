# EMA Hourly Continuation — ETN/USDT P26_89

**Symbol:** ETN/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.5299 |
| net_win_rate | 0.4021 |
| gross_profit_factor | 0.6629 |
| gross_win_rate | 0.4021 |
| sharpe_ratio | -4.2149 |
| sortino_ratio | -1.2798 |
| max_drawdown | 0.7150 |
| cagr | -0.4477 |
| net_avg_win | 51.5166 |
| net_avg_loss | -65.3669 |
| avg_hold_time_bars | 12.5412 |
| exposure | 0.2643 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
