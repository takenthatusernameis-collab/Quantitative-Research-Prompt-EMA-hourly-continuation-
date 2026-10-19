# EMA Hourly Continuation — VET/USDT P12_20

**Symbol:** VET/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1494 |
| net_profit_factor | 0.2312 |
| net_win_rate | 0.3889 |
| gross_profit_factor | 0.6694 |
| gross_win_rate | 0.4270 |
| sharpe_ratio | -14.5141 |
| sortino_ratio | -8.0461 |
| max_drawdown | 1.0000 |
| cagr | -0.9851 |
| net_avg_win | 5.1754 |
| net_avg_loss | -14.2460 |
| avg_hold_time_bars | 2.1693 |
| exposure | 0.1473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
