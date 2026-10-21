# EMA Hourly Continuation — HBAR/USDT P8_100

**Symbol:** HBAR/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 476 |
| net_profit_factor | 0.9694 |
| net_win_rate | 0.5504 |
| gross_profit_factor | 1.2085 |
| gross_win_rate | 0.5504 |
| sharpe_ratio | -0.1533 |
| sortino_ratio | -0.0485 |
| max_drawdown | 0.2782 |
| cagr | -0.0301 |
| net_avg_win | 89.2258 |
| net_avg_loss | -112.6886 |
| avg_hold_time_bars | 29.9181 |
| exposure | 0.6473 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
