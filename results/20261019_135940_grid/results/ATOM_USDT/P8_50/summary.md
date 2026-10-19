# EMA Hourly Continuation — ATOM/USDT P8_50

**Symbol:** ATOM/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 946 |
| net_profit_factor | 0.5019 |
| net_win_rate | 0.4630 |
| gross_profit_factor | 0.9333 |
| gross_win_rate | 0.4778 |
| sharpe_ratio | -6.3059 |
| sortino_ratio | -2.7159 |
| max_drawdown | 0.9658 |
| cagr | -0.7376 |
| net_avg_win | 22.2023 |
| net_avg_loss | -38.1440 |
| avg_hold_time_bars | 12.0581 |
| exposure | 0.5185 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
