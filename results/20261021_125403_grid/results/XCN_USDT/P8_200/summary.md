# EMA Hourly Continuation — XCN/USDT P8_200

**Symbol:** XCN/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.7164 |
| net_win_rate | 0.4634 |
| gross_profit_factor | 0.8590 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -2.0346 |
| sortino_ratio | -0.5538 |
| max_drawdown | 0.4762 |
| cagr | -0.2266 |
| net_avg_win | 70.2265 |
| net_avg_loss | -84.6608 |
| avg_hold_time_bars | 44.5285 |
| exposure | 0.7469 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
