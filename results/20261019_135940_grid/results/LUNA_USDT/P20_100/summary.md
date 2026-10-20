# EMA Hourly Continuation — LUNA/USDT P20_100

**Symbol:** LUNA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 791 |
| net_profit_factor | 0.4948 |
| net_win_rate | 0.4311 |
| gross_profit_factor | 0.8490 |
| gross_win_rate | 0.4437 |
| sharpe_ratio | -6.8750 |
| sortino_ratio | -2.7053 |
| max_drawdown | 0.9673 |
| cagr | -0.7429 |
| net_avg_win | 27.7789 |
| net_avg_loss | -42.5389 |
| avg_hold_time_bars | 10.5221 |
| exposure | 0.3783 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
