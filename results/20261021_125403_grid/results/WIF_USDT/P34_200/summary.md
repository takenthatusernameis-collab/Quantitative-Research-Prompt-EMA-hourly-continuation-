# EMA Hourly Continuation — WIF/USDT P34_200

**Symbol:** WIF/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 294 |
| net_profit_factor | 0.8091 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9280 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -1.0913 |
| sortino_ratio | -0.2665 |
| max_drawdown | 0.3487 |
| cagr | -0.1168 |
| net_avg_win | 79.9699 |
| net_avg_loss | -92.3368 |
| avg_hold_time_bars | 33.9354 |
| exposure | 0.4535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
