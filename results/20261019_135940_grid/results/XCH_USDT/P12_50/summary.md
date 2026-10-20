# EMA Hourly Continuation — XCH/USDT P12_50

**Symbol:** XCH/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1258 |
| net_profit_factor | 0.4567 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4467 |
| sharpe_ratio | -8.2277 |
| sortino_ratio | -4.0952 |
| max_drawdown | 0.9938 |
| cagr | -0.8659 |
| net_avg_win | 15.2435 |
| net_avg_loss | -25.7592 |
| avg_hold_time_bars | 6.5000 |
| exposure | 0.3717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
