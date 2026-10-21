# EMA Hourly Continuation — XEC/USDT P26_34

**Symbol:** XEC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.6580 |
| net_win_rate | 0.5093 |
| gross_profit_factor | 1.0623 |
| gross_win_rate | 0.5093 |
| sharpe_ratio | -2.4892 |
| sortino_ratio | -0.6453 |
| max_drawdown | 0.5815 |
| cagr | -0.2547 |
| net_avg_win | 61.0668 |
| net_avg_loss | -96.3056 |
| avg_hold_time_bars | 5.0926 |
| exposure | 0.0747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
