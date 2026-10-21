# EMA Hourly Continuation — UNI/USDT P26_50

**Symbol:** UNI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.6842 |
| net_win_rate | 0.4761 |
| gross_profit_factor | 0.9076 |
| gross_win_rate | 0.4761 |
| sharpe_ratio | -2.2362 |
| sortino_ratio | -0.6021 |
| max_drawdown | 0.5081 |
| cagr | -0.2408 |
| net_avg_win | 64.0233 |
| net_avg_loss | -85.0196 |
| avg_hold_time_bars | 6.7324 |
| exposure | 0.1086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
