# EMA Hourly Continuation — DUSK/USDT P55_200

**Symbol:** DUSK/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.8245 |
| net_win_rate | 0.4983 |
| gross_profit_factor | 0.9762 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -0.9739 |
| sortino_ratio | -0.2355 |
| max_drawdown | 0.2639 |
| cagr | -0.1044 |
| net_avg_win | 79.4597 |
| net_avg_loss | -95.7075 |
| avg_hold_time_bars | 27.7770 |
| exposure | 0.3624 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
