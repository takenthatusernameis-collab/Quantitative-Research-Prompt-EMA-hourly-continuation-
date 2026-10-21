# EMA Hourly Continuation — DGB/USDT P50_89

**Symbol:** DGB/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.7182 |
| net_win_rate | 0.4985 |
| gross_profit_factor | 0.9670 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -1.7134 |
| sortino_ratio | -0.4445 |
| max_drawdown | 0.4283 |
| cagr | -0.1841 |
| net_avg_win | 62.5542 |
| net_avg_loss | -86.5730 |
| avg_hold_time_bars | 7.6177 |
| exposure | 0.1132 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
