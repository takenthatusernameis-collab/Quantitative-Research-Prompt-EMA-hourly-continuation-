# EMA Hourly Continuation — EUL/USDT P26_55

**Symbol:** EUL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 833 |
| net_profit_factor | 0.3323 |
| net_win_rate | 0.4166 |
| gross_profit_factor | 0.5699 |
| gross_win_rate | 0.4262 |
| sharpe_ratio | -7.4593 |
| sortino_ratio | -3.0311 |
| max_drawdown | 0.9771 |
| cagr | -0.7747 |
| net_avg_win | 14.0057 |
| net_avg_loss | -30.0888 |
| avg_hold_time_bars | 4.8475 |
| exposure | 0.1835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
