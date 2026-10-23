# EMA Hourly Continuation — LSK/USDT P34_200

**Symbol:** LSK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 347 |
| net_profit_factor | 0.6439 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9253 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -2.5355 |
| sortino_ratio | -0.6594 |
| max_drawdown | 0.5994 |
| cagr | -0.2731 |
| net_avg_win | 60.7682 |
| net_avg_loss | -84.5757 |
| avg_hold_time_bars | 32.2594 |
| exposure | 0.5088 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
