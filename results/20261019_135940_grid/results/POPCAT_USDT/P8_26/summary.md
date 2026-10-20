# EMA Hourly Continuation — POPCAT/USDT P8_26

**Symbol:** POPCAT/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1339 |
| net_profit_factor | 0.5692 |
| net_win_rate | 0.4429 |
| gross_profit_factor | 0.8230 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -8.6195 |
| sortino_ratio | -4.7591 |
| max_drawdown | 0.9936 |
| cagr | -0.9031 |
| net_avg_win | 22.1369 |
| net_avg_loss | -30.9152 |
| avg_hold_time_bars | 4.1695 |
| exposure | 0.2949 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
