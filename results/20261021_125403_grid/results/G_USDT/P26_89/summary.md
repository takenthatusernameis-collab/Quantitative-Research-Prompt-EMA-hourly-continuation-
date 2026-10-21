# EMA Hourly Continuation — G/USDT P26_89

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.6233 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8348 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -3.5282 |
| sortino_ratio | -1.1372 |
| max_drawdown | 0.7004 |
| cagr | -0.4070 |
| net_avg_win | 56.1251 |
| net_avg_loss | -73.8089 |
| avg_hold_time_bars | 14.6532 |
| exposure | 0.3421 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
