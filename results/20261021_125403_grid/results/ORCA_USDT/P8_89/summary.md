# EMA Hourly Continuation — ORCA/USDT P8_89

**Symbol:** ORCA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 528 |
| net_profit_factor | 0.7900 |
| net_win_rate | 0.4981 |
| gross_profit_factor | 0.9674 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -1.5800 |
| sortino_ratio | -0.5183 |
| max_drawdown | 0.5068 |
| cagr | -0.2144 |
| net_avg_win | 65.0305 |
| net_avg_loss | -81.6913 |
| avg_hold_time_bars | 26.8409 |
| exposure | 0.6442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
