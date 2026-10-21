# EMA Hourly Continuation — XYO/USDT P21_200

**Symbol:** XYO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.6484 |
| net_win_rate | 0.4589 |
| gross_profit_factor | 0.8353 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -2.6303 |
| sortino_ratio | -0.7229 |
| max_drawdown | 0.6059 |
| cagr | -0.2840 |
| net_avg_win | 60.7151 |
| net_avg_loss | -79.4048 |
| avg_hold_time_bars | 34.8753 |
| exposure | 0.5950 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
