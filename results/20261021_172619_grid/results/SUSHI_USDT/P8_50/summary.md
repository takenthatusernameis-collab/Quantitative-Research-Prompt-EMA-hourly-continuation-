# EMA Hourly Continuation — SUSHI/USDT P8_50

**Symbol:** SUSHI/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.7538 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.9567 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -2.8227 |
| sortino_ratio | -1.0485 |
| max_drawdown | 0.7262 |
| cagr | -0.3830 |
| net_avg_win | 66.3249 |
| net_avg_loss | -80.1051 |
| avg_hold_time_bars | 14.5425 |
| exposure | 0.4488 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
