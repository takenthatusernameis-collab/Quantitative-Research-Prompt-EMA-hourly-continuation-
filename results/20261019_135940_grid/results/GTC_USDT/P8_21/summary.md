# EMA Hourly Continuation — GTC/USDT P8_21

**Symbol:** GTC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1419 |
| net_profit_factor | 0.4307 |
| net_win_rate | 0.4348 |
| gross_profit_factor | 0.9013 |
| gross_win_rate | 0.4531 |
| sharpe_ratio | -9.8747 |
| sortino_ratio | -5.2592 |
| max_drawdown | 0.9985 |
| cagr | -0.9244 |
| net_avg_win | 12.2436 |
| net_avg_loss | -21.8691 |
| avg_hold_time_bars | 3.8421 |
| exposure | 0.2478 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
