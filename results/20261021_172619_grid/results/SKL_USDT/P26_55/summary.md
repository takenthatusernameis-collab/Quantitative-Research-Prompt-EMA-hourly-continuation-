# EMA Hourly Continuation — SKL/USDT P26_55

**Symbol:** SKL/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.6217 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8187 |
| gross_win_rate | 0.4481 |
| sharpe_ratio | -3.3282 |
| sortino_ratio | -1.0178 |
| max_drawdown | 0.7085 |
| cagr | -0.3736 |
| net_avg_win | 54.8723 |
| net_avg_loss | -71.6446 |
| avg_hold_time_bars | 7.6667 |
| exposure | 0.1610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
