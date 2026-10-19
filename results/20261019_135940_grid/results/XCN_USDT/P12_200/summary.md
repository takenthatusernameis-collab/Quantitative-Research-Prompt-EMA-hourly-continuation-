# EMA Hourly Continuation — XCN/USDT P12_200

**Symbol:** XCN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.5785 |
| net_win_rate | 0.4568 |
| gross_profit_factor | 0.8441 |
| gross_win_rate | 0.4626 |
| sharpe_ratio | -3.7911 |
| sortino_ratio | -1.2181 |
| max_drawdown | 0.7645 |
| cagr | -0.4374 |
| net_avg_win | 44.0577 |
| net_avg_loss | -64.0529 |
| avg_hold_time_bars | 29.5278 |
| exposure | 0.6993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
