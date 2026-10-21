# EMA Hourly Continuation — METIS/USDT P12_200

**Symbol:** METIS/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 269 |
| net_profit_factor | 0.7758 |
| net_win_rate | 0.4758 |
| gross_profit_factor | 0.9027 |
| gross_win_rate | 0.4758 |
| sharpe_ratio | -1.3154 |
| sortino_ratio | -0.3063 |
| max_drawdown | 0.3373 |
| cagr | -0.1323 |
| net_avg_win | 81.0290 |
| net_avg_loss | -94.8137 |
| avg_hold_time_bars | 61.9703 |
| exposure | 0.7577 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
