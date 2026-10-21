# EMA Hourly Continuation — ETC/USDT P26_89

**Symbol:** ETC/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 467 |
| net_profit_factor | 0.6627 |
| net_win_rate | 0.4925 |
| gross_profit_factor | 0.9452 |
| gross_win_rate | 0.4925 |
| sharpe_ratio | -2.5744 |
| sortino_ratio | -0.7968 |
| max_drawdown | 0.6111 |
| cagr | -0.3054 |
| net_avg_win | 51.2152 |
| net_avg_loss | -75.0003 |
| avg_hold_time_bars | 12.8522 |
| exposure | 0.2728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
