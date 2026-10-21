# EMA Hourly Continuation — CYBER/USDT P144_200

**Symbol:** CYBER/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 224 |
| net_profit_factor | 0.7106 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9804 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.5143 |
| sortino_ratio | -0.3252 |
| max_drawdown | 0.3202 |
| cagr | -0.1392 |
| net_avg_win | 68.7632 |
| net_avg_loss | -96.7692 |
| avg_hold_time_bars | 8.2991 |
| exposure | 0.0845 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
