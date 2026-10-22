# EMA Hourly Continuation — APE/USDT P8_200

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.6380 |
| net_win_rate | 0.4813 |
| gross_profit_factor | 0.9323 |
| gross_win_rate | 0.4888 |
| sharpe_ratio | -2.0846 |
| sortino_ratio | -0.4780 |
| max_drawdown | 0.4370 |
| cagr | -0.2045 |
| net_avg_win | 59.6955 |
| net_avg_loss | -86.8400 |
| avg_hold_time_bars | 70.1567 |
| exposure | 0.8546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
