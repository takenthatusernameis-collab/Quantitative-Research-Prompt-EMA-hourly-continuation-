# EMA Hourly Continuation — DGB/USDT P20_50

**Symbol:** DGB/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.6538 |
| net_win_rate | 0.4612 |
| gross_profit_factor | 0.8782 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -3.0714 |
| sortino_ratio | -0.9561 |
| max_drawdown | 0.6774 |
| cagr | -0.3551 |
| net_avg_win | 57.3268 |
| net_avg_loss | -75.0536 |
| avg_hold_time_bars | 7.8700 |
| exposure | 0.1706 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
