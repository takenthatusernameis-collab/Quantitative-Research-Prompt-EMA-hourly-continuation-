# EMA Hourly Continuation — TRB/USDT P12_21

**Symbol:** TRB/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1600 |
| net_profit_factor | 0.3102 |
| net_win_rate | 0.3731 |
| gross_profit_factor | 0.7686 |
| gross_win_rate | 0.4131 |
| sharpe_ratio | -15.1528 |
| sortino_ratio | -8.6524 |
| max_drawdown | 1.0000 |
| cagr | -0.9889 |
| net_avg_win | 7.5312 |
| net_avg_loss | -14.4526 |
| avg_hold_time_bars | 2.2181 |
| exposure | 0.1606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
