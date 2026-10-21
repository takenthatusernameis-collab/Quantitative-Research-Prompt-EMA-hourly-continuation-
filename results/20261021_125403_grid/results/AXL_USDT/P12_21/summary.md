# EMA Hourly Continuation — AXL/USDT P12_21

**Symbol:** AXL/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 458 |
| net_profit_factor | 0.5637 |
| net_win_rate | 0.4214 |
| gross_profit_factor | 0.7727 |
| gross_win_rate | 0.4214 |
| sharpe_ratio | -4.3482 |
| sortino_ratio | -1.3201 |
| max_drawdown | 0.7889 |
| cagr | -0.4580 |
| net_avg_win | 52.6677 |
| net_avg_loss | -68.0467 |
| avg_hold_time_bars | 4.6004 |
| exposure | 0.0953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
