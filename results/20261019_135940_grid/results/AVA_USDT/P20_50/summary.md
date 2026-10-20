# EMA Hourly Continuation — AVA/USDT P20_50

**Symbol:** AVA/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 974 |
| net_profit_factor | 0.4385 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.8387 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -7.4635 |
| sortino_ratio | -3.2678 |
| max_drawdown | 0.9840 |
| cagr | -0.8043 |
| net_avg_win | 17.2945 |
| net_avg_loss | -33.0423 |
| avg_hold_time_bars | 4.5565 |
| exposure | 0.2017 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
