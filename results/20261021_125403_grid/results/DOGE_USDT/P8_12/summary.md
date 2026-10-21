# EMA Hourly Continuation — DOGE/USDT P8_12

**Symbol:** DOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 185 |
| net_profit_factor | 0.8450 |
| net_win_rate | 0.5514 |
| gross_profit_factor | 1.2186 |
| gross_win_rate | 0.5514 |
| sharpe_ratio | -0.6911 |
| sortino_ratio | -0.1364 |
| max_drawdown | 0.1854 |
| cagr | -0.0612 |
| net_avg_win | 78.3480 |
| net_avg_loss | -113.9484 |
| avg_hold_time_bars | 5.3243 |
| exposure | 0.0448 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
