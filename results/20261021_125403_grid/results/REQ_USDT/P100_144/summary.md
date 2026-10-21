# EMA Hourly Continuation — REQ/USDT P100_144

**Symbol:** REQ/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.4331 |
| net_win_rate | 0.3782 |
| gross_profit_factor | 0.6933 |
| gross_win_rate | 0.3855 |
| sharpe_ratio | -4.8359 |
| sortino_ratio | -1.1526 |
| max_drawdown | 0.7558 |
| cagr | -0.4184 |
| net_avg_win | 54.6260 |
| net_avg_loss | -76.7073 |
| avg_hold_time_bars | 7.3891 |
| exposure | 0.0924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
