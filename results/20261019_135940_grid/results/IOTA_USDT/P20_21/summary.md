# EMA Hourly Continuation — IOTA/USDT P20_21

**Symbol:** IOTA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1229 |
| net_profit_factor | 0.0758 |
| net_win_rate | 0.2937 |
| gross_profit_factor | 0.4647 |
| gross_win_rate | 0.3808 |
| sharpe_ratio | -18.0253 |
| sortino_ratio | -9.6436 |
| max_drawdown | 1.0000 |
| cagr | -0.9955 |
| net_avg_win | 2.2717 |
| net_avg_loss | -12.4655 |
| avg_hold_time_bars | 1.7234 |
| exposure | 0.0963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
