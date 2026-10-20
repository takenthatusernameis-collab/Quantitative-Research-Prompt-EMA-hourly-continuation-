# EMA Hourly Continuation — XCH/USDT P50_89

**Symbol:** XCH/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 755 |
| net_profit_factor | 0.3657 |
| net_win_rate | 0.4384 |
| gross_profit_factor | 0.7587 |
| gross_win_rate | 0.4464 |
| sharpe_ratio | -6.9255 |
| sortino_ratio | -2.6789 |
| max_drawdown | 0.9654 |
| cagr | -0.7367 |
| net_avg_win | 16.8067 |
| net_avg_loss | -35.8788 |
| avg_hold_time_bars | 5.0583 |
| exposure | 0.1736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
