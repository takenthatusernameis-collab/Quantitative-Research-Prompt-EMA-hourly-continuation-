# EMA Hourly Continuation — ENJ/USDT P100_200

**Symbol:** ENJ/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.8731 |
| net_win_rate | 0.5299 |
| gross_profit_factor | 1.1162 |
| gross_win_rate | 0.5299 |
| sharpe_ratio | -0.6071 |
| sortino_ratio | -0.1336 |
| max_drawdown | 0.1788 |
| cagr | -0.0615 |
| net_avg_win | 82.1396 |
| net_avg_loss | -106.0521 |
| avg_hold_time_bars | 18.1667 |
| exposure | 0.1924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
