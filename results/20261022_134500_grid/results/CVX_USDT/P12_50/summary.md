# EMA Hourly Continuation — CVX/USDT P12_50

**Symbol:** CVX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1087 |
| net_profit_factor | 0.5549 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.8468 |
| gross_win_rate | 0.4747 |
| sharpe_ratio | -5.7388 |
| sortino_ratio | -2.6624 |
| max_drawdown | 0.9603 |
| cagr | -0.7214 |
| net_avg_win | 23.5480 |
| net_avg_loss | -37.2343 |
| avg_hold_time_bars | 6.7617 |
| exposure | 0.3341 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
