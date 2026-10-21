# EMA Hourly Continuation — SOL/USDT P26_100

**Symbol:** SOL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.8205 |
| net_win_rate | 0.5200 |
| gross_profit_factor | 1.0841 |
| gross_win_rate | 0.5200 |
| sharpe_ratio | -1.2682 |
| sortino_ratio | -0.3650 |
| max_drawdown | 0.3849 |
| cagr | -0.1554 |
| net_avg_win | 75.9871 |
| net_avg_loss | -100.3226 |
| avg_hold_time_bars | 14.9450 |
| exposure | 0.2717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
