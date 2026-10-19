# EMA Hourly Continuation — THETA/USDT P8_100

**Symbol:** THETA/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 611 |
| net_profit_factor | 0.6758 |
| net_win_rate | 0.4795 |
| gross_profit_factor | 0.9825 |
| gross_win_rate | 0.4910 |
| sharpe_ratio | -3.2519 |
| sortino_ratio | -1.1298 |
| max_drawdown | 0.7596 |
| cagr | -0.4185 |
| net_avg_win | 52.9051 |
| net_avg_loss | -72.1328 |
| avg_hold_time_bars | 24.6727 |
| exposure | 0.6852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
