# EMA Hourly Continuation — MINA/USDT P26_34

**Symbol:** MINA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 277 |
| net_profit_factor | 0.6418 |
| net_win_rate | 0.4838 |
| gross_profit_factor | 0.9737 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -2.5339 |
| sortino_ratio | -0.6053 |
| max_drawdown | 0.5543 |
| cagr | -0.2432 |
| net_avg_win | 67.2927 |
| net_avg_loss | -98.2525 |
| avg_hold_time_bars | 5.1444 |
| exposure | 0.0648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
