# EMA Hourly Continuation — AURORA/USDT P21_200

**Symbol:** AURORA/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.5587 |
| net_win_rate | 0.4373 |
| gross_profit_factor | 0.8230 |
| gross_win_rate | 0.4472 |
| sharpe_ratio | -3.8934 |
| sortino_ratio | -1.0999 |
| max_drawdown | 0.7520 |
| cagr | -0.4133 |
| net_avg_win | 52.4884 |
| net_avg_loss | -73.0249 |
| avg_hold_time_bars | 30.4005 |
| exposure | 0.5624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
