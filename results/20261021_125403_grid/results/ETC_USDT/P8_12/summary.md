# EMA Hourly Continuation — ETC/USDT P8_12

**Symbol:** ETC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 238 |
| net_profit_factor | 0.5921 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9601 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.3119 |
| sortino_ratio | -0.5140 |
| max_drawdown | 0.4497 |
| cagr | -0.2089 |
| net_avg_win | 54.2653 |
| net_avg_loss | -91.6438 |
| avg_hold_time_bars | 4.2773 |
| exposure | 0.0463 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
