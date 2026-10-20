# EMA Hourly Continuation — IOST/USDT P21_200

**Symbol:** IOST/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.7912 |
| net_win_rate | 0.5260 |
| gross_profit_factor | 1.1267 |
| gross_win_rate | 0.5312 |
| sharpe_ratio | -1.4264 |
| sortino_ratio | -0.3955 |
| max_drawdown | 0.4499 |
| cagr | -0.1729 |
| net_avg_win | 71.1164 |
| net_avg_loss | -99.7627 |
| avg_hold_time_bars | 36.1042 |
| exposure | 0.6302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
