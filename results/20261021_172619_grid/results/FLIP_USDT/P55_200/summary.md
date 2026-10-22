# EMA Hourly Continuation — FLIP/USDT P55_200

**Symbol:** FLIP/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 234 |
| net_profit_factor | 0.6129 |
| net_win_rate | 0.4444 |
| gross_profit_factor | 0.7909 |
| gross_win_rate | 0.4444 |
| sharpe_ratio | -2.3247 |
| sortino_ratio | -0.5007 |
| max_drawdown | 0.4668 |
| cagr | -0.2091 |
| net_avg_win | 67.7914 |
| net_avg_loss | -88.4831 |
| avg_hold_time_bars | 32.8547 |
| exposure | 0.3495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
