# EMA Hourly Continuation — CARV/USDT P50_55

**Symbol:** CARV/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 149 |
| net_profit_factor | 0.5995 |
| net_win_rate | 0.4899 |
| gross_profit_factor | 1.0103 |
| gross_win_rate | 0.5034 |
| sharpe_ratio | -2.1019 |
| sortino_ratio | -0.4111 |
| max_drawdown | 0.3242 |
| cagr | -0.1707 |
| net_avg_win | 64.7965 |
| net_avg_loss | -103.8115 |
| avg_hold_time_bars | 4.1208 |
| exposure | 0.0346 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
