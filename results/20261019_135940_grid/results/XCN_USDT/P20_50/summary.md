# EMA Hourly Continuation — XCN/USDT P20_50

**Symbol:** XCN/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1220 |
| net_profit_factor | 0.3087 |
| net_win_rate | 0.3754 |
| gross_profit_factor | 0.6354 |
| gross_win_rate | 0.4033 |
| sharpe_ratio | -11.6562 |
| sortino_ratio | -5.7392 |
| max_drawdown | 0.9994 |
| cagr | -0.9488 |
| net_avg_win | 9.7451 |
| net_avg_loss | -18.9732 |
| avg_hold_time_bars | 4.2475 |
| exposure | 0.2355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
