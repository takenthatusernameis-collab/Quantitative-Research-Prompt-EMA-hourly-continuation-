# EMA Hourly Continuation — LINK/USDT P12_21

**Symbol:** LINK/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.6898 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9896 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -1.9643 |
| sortino_ratio | -0.4522 |
| max_drawdown | 0.4667 |
| cagr | -0.1871 |
| net_avg_win | 71.0061 |
| net_avg_loss | -100.5640 |
| avg_hold_time_bars | 5.3307 |
| exposure | 0.0623 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
