# EMA Hourly Continuation — ETH/USDT P21_50

**Symbol:** ETH/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.6409 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0013 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.7304 |
| sortino_ratio | -0.7860 |
| max_drawdown | 0.5984 |
| cagr | -0.2999 |
| net_avg_win | 52.7923 |
| net_avg_loss | -82.3663 |
| avg_hold_time_bars | 8.6525 |
| exposure | 0.1573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
