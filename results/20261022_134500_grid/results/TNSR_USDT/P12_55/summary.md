# EMA Hourly Continuation — TNSR/USDT P12_55

**Symbol:** TNSR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 967 |
| net_profit_factor | 0.6657 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.9651 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -5.0178 |
| sortino_ratio | -2.1796 |
| max_drawdown | 0.9310 |
| cagr | -0.6514 |
| net_avg_win | 40.8738 |
| net_avg_loss | -54.1150 |
| avg_hold_time_bars | 9.0331 |
| exposure | 0.3953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
