# EMA Hourly Continuation — DGB/USDT P26_55

**Symbol:** DGB/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1028 |
| net_profit_factor | 0.4254 |
| net_win_rate | 0.4300 |
| gross_profit_factor | 0.8505 |
| gross_win_rate | 0.4465 |
| sharpe_ratio | -8.9119 |
| sortino_ratio | -4.0175 |
| max_drawdown | 0.9941 |
| cagr | -0.8695 |
| net_avg_win | 16.6462 |
| net_avg_loss | -29.5178 |
| avg_hold_time_bars | 3.9280 |
| exposure | 0.1835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
