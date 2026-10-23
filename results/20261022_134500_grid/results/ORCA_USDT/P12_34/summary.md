# EMA Hourly Continuation — ORCA/USDT P12_34

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1122 |
| net_profit_factor | 0.6108 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 1.0305 |
| gross_win_rate | 0.4982 |
| sharpe_ratio | -6.1615 |
| sortino_ratio | -2.9048 |
| max_drawdown | 0.9740 |
| cagr | -0.7571 |
| net_avg_win | 28.4367 |
| net_avg_loss | -42.5868 |
| avg_hold_time_bars | 5.3360 |
| exposure | 0.2721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
