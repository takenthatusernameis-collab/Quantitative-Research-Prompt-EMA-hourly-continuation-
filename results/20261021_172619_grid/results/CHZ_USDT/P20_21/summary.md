# EMA Hourly Continuation — CHZ/USDT P20_21

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 133 |
| net_profit_factor | 0.7919 |
| net_win_rate | 0.5338 |
| gross_profit_factor | 1.1427 |
| gross_win_rate | 0.5338 |
| sharpe_ratio | -0.8294 |
| sortino_ratio | -0.1385 |
| max_drawdown | 0.2389 |
| cagr | -0.0612 |
| net_avg_win | 78.6392 |
| net_avg_loss | -113.7176 |
| avg_hold_time_bars | 5.0752 |
| exposure | 0.0307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
