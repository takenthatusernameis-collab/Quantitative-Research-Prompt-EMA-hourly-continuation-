# EMA Hourly Continuation — LUNC/USDT P50_200

**Symbol:** LUNC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.8040 |
| net_win_rate | 0.5110 |
| gross_profit_factor | 1.0308 |
| gross_win_rate | 0.5110 |
| sharpe_ratio | -1.1410 |
| sortino_ratio | -0.2916 |
| max_drawdown | 0.3250 |
| cagr | -0.1263 |
| net_avg_win | 72.7836 |
| net_avg_loss | -94.6192 |
| avg_hold_time_bars | 25.4006 |
| exposure | 0.3660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
