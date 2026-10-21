# EMA Hourly Continuation — TRB/USDT P12_20

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.5374 |
| net_win_rate | 0.4183 |
| gross_profit_factor | 0.7649 |
| gross_win_rate | 0.4183 |
| sharpe_ratio | -3.7930 |
| sortino_ratio | -0.9440 |
| max_drawdown | 0.6833 |
| cagr | -0.3537 |
| net_avg_win | 60.5758 |
| net_avg_loss | -81.0630 |
| avg_hold_time_bars | 4.8399 |
| exposure | 0.0670 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
