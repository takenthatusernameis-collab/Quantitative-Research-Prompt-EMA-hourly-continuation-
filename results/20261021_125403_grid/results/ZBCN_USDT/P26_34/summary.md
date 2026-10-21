# EMA Hourly Continuation — ZBCN/USDT P26_34

**Symbol:** ZBCN/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 127 |
| net_profit_factor | 1.0195 |
| net_win_rate | 0.5669 |
| gross_profit_factor | 1.2952 |
| gross_win_rate | 0.5669 |
| sharpe_ratio | 0.1063 |
| sortino_ratio | 0.0176 |
| max_drawdown | 0.0913 |
| cagr | 0.0051 |
| net_avg_win | 90.9289 |
| net_avg_loss | -116.7570 |
| avg_hold_time_bars | 5.3622 |
| exposure | 0.0315 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
