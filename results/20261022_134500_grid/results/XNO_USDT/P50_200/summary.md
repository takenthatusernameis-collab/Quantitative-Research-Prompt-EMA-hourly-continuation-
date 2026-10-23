# EMA Hourly Continuation — XNO/USDT P50_200

**Symbol:** XNO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.5116 |
| net_win_rate | 0.4236 |
| gross_profit_factor | 0.7453 |
| gross_win_rate | 0.4255 |
| sharpe_ratio | -5.0027 |
| sortino_ratio | -1.6577 |
| max_drawdown | 0.8602 |
| cagr | -0.5432 |
| net_avg_win | 38.6709 |
| net_avg_loss | -55.5593 |
| avg_hold_time_bars | 14.5964 |
| exposure | 0.3649 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
