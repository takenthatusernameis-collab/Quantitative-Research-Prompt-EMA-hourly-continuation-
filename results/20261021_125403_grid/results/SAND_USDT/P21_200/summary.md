# EMA Hourly Continuation — SAND/USDT P21_200

**Symbol:** SAND/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.7250 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.8815 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -1.4699 |
| sortino_ratio | -0.3135 |
| max_drawdown | 0.3186 |
| cagr | -0.1348 |
| net_avg_win | 75.8376 |
| net_avg_loss | -93.1763 |
| avg_hold_time_bars | 68.0578 |
| exposure | 0.6960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
