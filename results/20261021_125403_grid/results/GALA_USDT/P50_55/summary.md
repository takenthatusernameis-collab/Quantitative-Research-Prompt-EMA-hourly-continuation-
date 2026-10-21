# EMA Hourly Continuation — GALA/USDT P50_55

**Symbol:** GALA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 130 |
| net_profit_factor | 0.4362 |
| net_win_rate | 0.3692 |
| gross_profit_factor | 0.6063 |
| gross_win_rate | 0.3692 |
| sharpe_ratio | -3.0036 |
| sortino_ratio | -0.4865 |
| max_drawdown | 0.4408 |
| cagr | -0.2018 |
| net_avg_win | 69.6427 |
| net_avg_loss | -93.4687 |
| avg_hold_time_bars | 3.9308 |
| exposure | 0.0232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
