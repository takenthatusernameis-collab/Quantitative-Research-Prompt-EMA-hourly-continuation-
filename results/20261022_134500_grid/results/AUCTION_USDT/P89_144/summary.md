# EMA Hourly Continuation — AUCTION/USDT P89_144

**Symbol:** AUCTION/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 514 |
| net_profit_factor | 0.3738 |
| net_win_rate | 0.4105 |
| gross_profit_factor | 0.6947 |
| gross_win_rate | 0.4222 |
| sharpe_ratio | -6.8181 |
| sortino_ratio | -2.1698 |
| max_drawdown | 0.9369 |
| cagr | -0.6657 |
| net_avg_win | 26.5030 |
| net_avg_loss | -49.3777 |
| avg_hold_time_bars | 6.4183 |
| exposure | 0.1493 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
