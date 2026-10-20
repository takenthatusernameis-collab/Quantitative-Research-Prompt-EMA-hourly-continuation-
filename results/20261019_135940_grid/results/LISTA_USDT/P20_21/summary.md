# EMA Hourly Continuation — LISTA/USDT P20_21

**Symbol:** LISTA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1039 |
| net_profit_factor | 0.2389 |
| net_win_rate | 0.3282 |
| gross_profit_factor | 0.7775 |
| gross_win_rate | 0.4167 |
| sharpe_ratio | -14.6706 |
| sortino_ratio | -7.1582 |
| max_drawdown | 0.9999 |
| cagr | -0.9794 |
| net_avg_win | 9.2026 |
| net_avg_loss | -18.8208 |
| avg_hold_time_bars | 2.3792 |
| exposure | 0.1209 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
