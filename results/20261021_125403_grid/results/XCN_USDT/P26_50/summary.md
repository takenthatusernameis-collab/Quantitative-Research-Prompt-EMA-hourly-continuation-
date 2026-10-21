# EMA Hourly Continuation — XCN/USDT P26_50

**Symbol:** XCN/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.6043 |
| net_win_rate | 0.4471 |
| gross_profit_factor | 0.8157 |
| gross_win_rate | 0.4471 |
| sharpe_ratio | -3.1368 |
| sortino_ratio | -0.8680 |
| max_drawdown | 0.6356 |
| cagr | -0.3292 |
| net_avg_win | 57.2049 |
| net_avg_loss | -76.5466 |
| avg_hold_time_bars | 6.6772 |
| exposure | 0.1147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
