# EMA Hourly Continuation — SUI/USDT P12_34

**Symbol:** SUI/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 540 |
| net_profit_factor | 0.7794 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 1.0108 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -2.0198 |
| sortino_ratio | -0.6726 |
| max_drawdown | 0.5723 |
| cagr | -0.2659 |
| net_avg_win | 70.9059 |
| net_avg_loss | -90.3070 |
| avg_hold_time_bars | 7.2870 |
| exposure | 0.1789 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
