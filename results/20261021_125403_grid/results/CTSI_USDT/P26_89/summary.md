# EMA Hourly Continuation — CTSI/USDT P26_89

**Symbol:** CTSI/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 573 |
| net_profit_factor | 0.7265 |
| net_win_rate | 0.4729 |
| gross_profit_factor | 0.9496 |
| gross_win_rate | 0.4729 |
| sharpe_ratio | -2.9063 |
| sortino_ratio | -0.9925 |
| max_drawdown | 0.6985 |
| cagr | -0.3657 |
| net_avg_win | 66.7785 |
| net_avg_loss | -82.4789 |
| avg_hold_time_bars | 11.6894 |
| exposure | 0.3045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
