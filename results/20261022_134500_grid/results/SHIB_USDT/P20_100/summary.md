# EMA Hourly Continuation — SHIB/USDT P20_100

**Symbol:** SHIB/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6082 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9718 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -4.5943 |
| sortino_ratio | -1.6728 |
| max_drawdown | 0.8736 |
| cagr | -0.5582 |
| net_avg_win | 42.1459 |
| net_avg_loss | -62.6572 |
| avg_hold_time_bars | 12.4734 |
| exposure | 0.3833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
