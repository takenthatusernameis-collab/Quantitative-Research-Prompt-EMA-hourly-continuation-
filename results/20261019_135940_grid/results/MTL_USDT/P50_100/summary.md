# EMA Hourly Continuation — MTL/USDT P50_100

**Symbol:** MTL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.4665 |
| net_win_rate | 0.4228 |
| gross_profit_factor | 0.8095 |
| gross_win_rate | 0.4463 |
| sharpe_ratio | -6.1703 |
| sortino_ratio | -2.1112 |
| max_drawdown | 0.9288 |
| cagr | -0.6471 |
| net_avg_win | 32.1852 |
| net_avg_loss | -50.5461 |
| avg_hold_time_bars | 8.2550 |
| exposure | 0.2226 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
