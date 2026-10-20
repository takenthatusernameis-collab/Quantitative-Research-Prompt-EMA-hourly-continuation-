# EMA Hourly Continuation — XCH/USDT P89_100

**Symbol:** XCH/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.1606 |
| net_win_rate | 0.3460 |
| gross_profit_factor | 0.6089 |
| gross_win_rate | 0.3854 |
| sharpe_ratio | -10.8542 |
| sortino_ratio | -4.0530 |
| max_drawdown | 0.9959 |
| cagr | -0.8883 |
| net_avg_win | 8.3582 |
| net_avg_loss | -27.5289 |
| avg_hold_time_bars | 2.0637 |
| exposure | 0.0618 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
