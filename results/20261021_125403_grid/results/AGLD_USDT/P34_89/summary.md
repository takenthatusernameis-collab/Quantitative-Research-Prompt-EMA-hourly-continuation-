# EMA Hourly Continuation — AGLD/USDT P34_89

**Symbol:** AGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 508 |
| net_profit_factor | 0.7218 |
| net_win_rate | 0.4724 |
| gross_profit_factor | 0.9429 |
| gross_win_rate | 0.4724 |
| sharpe_ratio | -2.7327 |
| sortino_ratio | -0.8759 |
| max_drawdown | 0.6976 |
| cagr | -0.3312 |
| net_avg_win | 68.9064 |
| net_avg_loss | -85.4942 |
| avg_hold_time_bars | 10.4626 |
| exposure | 0.2405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
