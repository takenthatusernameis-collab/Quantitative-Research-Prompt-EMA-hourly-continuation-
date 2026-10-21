# EMA Hourly Continuation — OGN/USDT P12_26

**Symbol:** OGN/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.6680 |
| net_win_rate | 0.4931 |
| gross_profit_factor | 1.0059 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -3.3553 |
| sortino_ratio | -1.1537 |
| max_drawdown | 0.7388 |
| cagr | -0.4105 |
| net_avg_win | 52.1694 |
| net_avg_loss | -75.9593 |
| avg_hold_time_bars | 5.5694 |
| exposure | 0.1452 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
