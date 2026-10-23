# EMA Hourly Continuation — ORCA/USDT P20_55

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 853 |
| net_profit_factor | 0.5621 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.9128 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -5.4797 |
| sortino_ratio | -2.2314 |
| max_drawdown | 0.9412 |
| cagr | -0.6697 |
| net_avg_win | 29.8112 |
| net_avg_loss | -47.7164 |
| avg_hold_time_bars | 6.7046 |
| exposure | 0.2600 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
