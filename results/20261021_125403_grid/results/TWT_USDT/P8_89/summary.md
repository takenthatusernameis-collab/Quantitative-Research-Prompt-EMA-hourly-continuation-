# EMA Hourly Continuation — TWT/USDT P8_89

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 578 |
| net_profit_factor | 0.8190 |
| net_win_rate | 0.5208 |
| gross_profit_factor | 1.0682 |
| gross_win_rate | 0.5208 |
| sharpe_ratio | -1.3897 |
| sortino_ratio | -0.4806 |
| max_drawdown | 0.4722 |
| cagr | -0.2002 |
| net_avg_win | 64.5550 |
| net_avg_loss | -85.6476 |
| avg_hold_time_bars | 23.8927 |
| exposure | 0.6277 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
