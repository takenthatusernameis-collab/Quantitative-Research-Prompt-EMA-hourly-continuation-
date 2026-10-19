# EMA Hourly Continuation — SHIB/USDT P50_200

**Symbol:** SHIB/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.5254 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8857 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -4.1079 |
| sortino_ratio | -1.1030 |
| max_drawdown | 0.7645 |
| cagr | -0.4300 |
| net_avg_win | 48.9655 |
| net_avg_loss | -76.9843 |
| avg_hold_time_bars | 22.5423 |
| exposure | 0.3873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
