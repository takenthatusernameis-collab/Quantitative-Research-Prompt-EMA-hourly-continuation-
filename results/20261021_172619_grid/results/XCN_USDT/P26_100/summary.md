# EMA Hourly Continuation — XCN/USDT P26_100

**Symbol:** XCN/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7120 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.9008 |
| gross_win_rate | 0.4733 |
| sharpe_ratio | -2.2782 |
| sortino_ratio | -0.6736 |
| max_drawdown | 0.5493 |
| cagr | -0.2665 |
| net_avg_win | 65.5278 |
| net_avg_loss | -82.7120 |
| avg_hold_time_bars | 17.0186 |
| exposure | 0.3334 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
