# EMA Hourly Continuation — LUNC/USDT P144_200

**Symbol:** LUNC/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 188 |
| net_profit_factor | 0.8195 |
| net_win_rate | 0.5426 |
| gross_profit_factor | 1.1714 |
| gross_win_rate | 0.5426 |
| sharpe_ratio | -0.7991 |
| sortino_ratio | -0.1589 |
| max_drawdown | 0.2122 |
| cagr | -0.0703 |
| net_avg_win | 74.4810 |
| net_avg_loss | -107.7980 |
| avg_hold_time_bars | 8.9415 |
| exposure | 0.0764 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
