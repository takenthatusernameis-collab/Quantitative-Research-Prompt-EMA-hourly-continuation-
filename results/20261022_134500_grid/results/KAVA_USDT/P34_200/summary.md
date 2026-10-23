# EMA Hourly Continuation — KAVA/USDT P34_200

**Symbol:** KAVA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.6337 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.9998 |
| gross_win_rate | 0.4895 |
| sharpe_ratio | -3.4707 |
| sortino_ratio | -1.0036 |
| max_drawdown | 0.7163 |
| cagr | -0.3872 |
| net_avg_win | 61.2094 |
| net_avg_loss | -85.1010 |
| avg_hold_time_bars | 25.7400 |
| exposure | 0.4996 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
