# EMA Hourly Continuation — TIA/USDT P12_21

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1474 |
| net_profit_factor | 0.3694 |
| net_win_rate | 0.4125 |
| gross_profit_factor | 0.7765 |
| gross_win_rate | 0.4342 |
| sharpe_ratio | -12.1140 |
| sortino_ratio | -6.5737 |
| max_drawdown | 0.9998 |
| cagr | -0.9662 |
| net_avg_win | 9.6346 |
| net_avg_loss | -18.3093 |
| avg_hold_time_bars | 2.0821 |
| exposure | 0.1395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
