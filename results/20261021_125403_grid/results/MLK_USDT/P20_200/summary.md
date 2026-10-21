# EMA Hourly Continuation — MLK/USDT P20_200

**Symbol:** MLK/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.5318 |
| net_win_rate | 0.3778 |
| gross_profit_factor | 0.6617 |
| gross_win_rate | 0.3778 |
| sharpe_ratio | -4.4378 |
| sortino_ratio | -1.2404 |
| max_drawdown | 0.7733 |
| cagr | -0.4398 |
| net_avg_win | 58.1745 |
| net_avg_loss | -66.4264 |
| avg_hold_time_bars | 30.0680 |
| exposure | 0.5402 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
