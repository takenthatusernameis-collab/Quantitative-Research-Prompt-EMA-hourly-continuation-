# EMA Hourly Continuation — MTL/USDT P100_200

**Symbol:** MTL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.4411 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.7794 |
| gross_win_rate | 0.4538 |
| sharpe_ratio | -4.4267 |
| sortino_ratio | -1.1803 |
| max_drawdown | 0.7748 |
| cagr | -0.4452 |
| net_avg_win | 38.1730 |
| net_avg_loss | -66.5650 |
| avg_hold_time_bars | 12.6033 |
| exposure | 0.2099 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
