# EMA Hourly Continuation — TAIKO/USDT P20_55

**Symbol:** TAIKO/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 507 |
| net_profit_factor | 0.7259 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9768 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -2.4313 |
| sortino_ratio | -0.8063 |
| max_drawdown | 0.6539 |
| cagr | -0.3091 |
| net_avg_win | 61.6958 |
| net_avg_loss | -83.3289 |
| avg_hold_time_bars | 9.0256 |
| exposure | 0.2198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
