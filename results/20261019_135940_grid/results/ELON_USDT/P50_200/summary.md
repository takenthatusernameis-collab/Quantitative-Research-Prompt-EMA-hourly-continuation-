# EMA Hourly Continuation — ELON/USDT P50_200

**Symbol:** ELON/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.5287 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7430 |
| gross_win_rate | 0.4313 |
| sharpe_ratio | -3.6648 |
| sortino_ratio | -1.0002 |
| max_drawdown | 0.6906 |
| cagr | -0.3697 |
| net_avg_win | 48.4198 |
| net_avg_loss | -68.6855 |
| avg_hold_time_bars | 22.3208 |
| exposure | 0.3764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
