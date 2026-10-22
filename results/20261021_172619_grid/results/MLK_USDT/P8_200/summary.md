# EMA Hourly Continuation — MLK/USDT P8_200

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.5916 |
| net_win_rate | 0.4131 |
| gross_profit_factor | 0.7282 |
| gross_win_rate | 0.4131 |
| sharpe_ratio | -3.5989 |
| sortino_ratio | -1.0443 |
| max_drawdown | 0.7128 |
| cagr | -0.3841 |
| net_avg_win | 58.0694 |
| net_avg_loss | -69.1017 |
| avg_hold_time_bars | 33.9977 |
| exposure | 0.6554 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
