# EMA Hourly Continuation — XCN/USDT P20_55

**Symbol:** XCN/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1170 |
| net_profit_factor | 0.3350 |
| net_win_rate | 0.3821 |
| gross_profit_factor | 0.6654 |
| gross_win_rate | 0.4094 |
| sharpe_ratio | -10.8698 |
| sortino_ratio | -5.2413 |
| max_drawdown | 0.9988 |
| cagr | -0.9311 |
| net_avg_win | 11.2547 |
| net_avg_loss | -20.7729 |
| avg_hold_time_bars | 4.8120 |
| exposure | 0.2559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
