# EMA Hourly Continuation — LUNC/USDT P21_26

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1245 |
| net_profit_factor | 0.1628 |
| net_win_rate | 0.3052 |
| gross_profit_factor | 0.6164 |
| gross_win_rate | 0.3647 |
| sharpe_ratio | -17.3406 |
| sortino_ratio | -9.1601 |
| max_drawdown | 1.0000 |
| cagr | -0.9933 |
| net_avg_win | 5.1188 |
| net_avg_loss | -13.8094 |
| avg_hold_time_bars | 1.8064 |
| exposure | 0.1022 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
