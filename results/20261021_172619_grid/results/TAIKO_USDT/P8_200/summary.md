# EMA Hourly Continuation — TAIKO/USDT P8_200

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 0.8309 |
| net_win_rate | 0.4965 |
| gross_profit_factor | 0.9916 |
| gross_win_rate | 0.4965 |
| sharpe_ratio | -1.0488 |
| sortino_ratio | -0.2615 |
| max_drawdown | 0.3285 |
| cagr | -0.1147 |
| net_avg_win | 86.3656 |
| net_avg_loss | -102.5066 |
| avg_hold_time_bars | 57.7604 |
| exposure | 0.7991 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
