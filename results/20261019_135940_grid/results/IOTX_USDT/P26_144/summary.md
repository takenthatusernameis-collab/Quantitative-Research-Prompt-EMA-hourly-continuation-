# EMA Hourly Continuation — IOTX/USDT P26_144

**Symbol:** IOTX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.6161 |
| net_win_rate | 0.4708 |
| gross_profit_factor | 0.8974 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -3.3937 |
| sortino_ratio | -1.1034 |
| max_drawdown | 0.7334 |
| cagr | -0.4066 |
| net_avg_win | 46.8902 |
| net_avg_loss | -67.7065 |
| avg_hold_time_bars | 19.5800 |
| exposure | 0.4726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
