# EMA Hourly Continuation — REQ/USDT P20_50

**Symbol:** REQ/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1089 |
| net_profit_factor | 0.4296 |
| net_win_rate | 0.4077 |
| gross_profit_factor | 0.9189 |
| gross_win_rate | 0.4435 |
| sharpe_ratio | -10.6222 |
| sortino_ratio | -5.0030 |
| max_drawdown | 0.9983 |
| cagr | -0.9198 |
| net_avg_win | 16.9306 |
| net_avg_loss | -27.1309 |
| avg_hold_time_bars | 5.3719 |
| exposure | 0.2659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
