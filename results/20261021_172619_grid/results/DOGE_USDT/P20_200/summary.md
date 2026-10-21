# EMA Hourly Continuation — DOGE/USDT P20_200

**Symbol:** DOGE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 268 |
| net_profit_factor | 0.7998 |
| net_win_rate | 0.4963 |
| gross_profit_factor | 0.9948 |
| gross_win_rate | 0.4963 |
| sharpe_ratio | -1.2100 |
| sortino_ratio | -0.2831 |
| max_drawdown | 0.3633 |
| cagr | -0.1226 |
| net_avg_win | 84.1115 |
| net_avg_loss | -103.6046 |
| avg_hold_time_bars | 53.8433 |
| exposure | 0.6559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
