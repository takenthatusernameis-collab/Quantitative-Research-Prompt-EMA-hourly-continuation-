# EMA Hourly Continuation — MLK/USDT P26_100

**Symbol:** MLK/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 899 |
| net_profit_factor | 0.3125 |
| net_win_rate | 0.3014 |
| gross_profit_factor | 0.5648 |
| gross_win_rate | 0.3126 |
| sharpe_ratio | -11.7635 |
| sortino_ratio | -5.0033 |
| max_drawdown | 0.9983 |
| cagr | -0.9186 |
| net_avg_win | 16.7426 |
| net_avg_loss | -23.1200 |
| avg_hold_time_bars | 8.6452 |
| exposure | 0.3517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
