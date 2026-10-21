# EMA Hourly Continuation — XCH/USDT P26_50

**Symbol:** XCH/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6919 |
| net_win_rate | 0.4837 |
| gross_profit_factor | 0.9450 |
| gross_win_rate | 0.4837 |
| sharpe_ratio | -2.3126 |
| sortino_ratio | -0.6615 |
| max_drawdown | 0.5416 |
| cagr | -0.2613 |
| net_avg_win | 61.9665 |
| net_avg_loss | -83.9087 |
| avg_hold_time_bars | 5.9875 |
| exposure | 0.1086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
