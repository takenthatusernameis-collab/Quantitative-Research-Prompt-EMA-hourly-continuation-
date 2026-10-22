# EMA Hourly Continuation — XCH/USDT P8_34

**Symbol:** XCH/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 715 |
| net_profit_factor | 0.6333 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8437 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -3.4779 |
| sortino_ratio | -1.3254 |
| max_drawdown | 0.7868 |
| cagr | -0.4557 |
| net_avg_win | 40.7308 |
| net_avg_loss | -55.7480 |
| avg_hold_time_bars | 8.2937 |
| exposure | 0.2695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
