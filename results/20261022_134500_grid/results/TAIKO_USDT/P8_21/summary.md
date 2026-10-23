# EMA Hourly Continuation — TAIKO/USDT P8_21

**Symbol:** TAIKO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1508 |
| net_profit_factor | 0.5078 |
| net_win_rate | 0.4324 |
| gross_profit_factor | 1.0236 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -11.6122 |
| sortino_ratio | -6.5059 |
| max_drawdown | 0.9997 |
| cagr | -0.9651 |
| net_avg_win | 15.8155 |
| net_avg_loss | -23.7246 |
| avg_hold_time_bars | 3.3475 |
| exposure | 0.2425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
