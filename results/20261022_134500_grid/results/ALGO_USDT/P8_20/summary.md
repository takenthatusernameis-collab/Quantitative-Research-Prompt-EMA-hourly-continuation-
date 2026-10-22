# EMA Hourly Continuation — ALGO/USDT P8_20

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1635 |
| net_profit_factor | 0.3072 |
| net_win_rate | 0.4391 |
| gross_profit_factor | 0.7310 |
| gross_win_rate | 0.4679 |
| sharpe_ratio | -11.4966 |
| sortino_ratio | -6.5615 |
| max_drawdown | 0.9998 |
| cagr | -0.9641 |
| net_avg_win | 6.1752 |
| net_avg_loss | -15.7376 |
| avg_hold_time_bars | 2.7260 |
| exposure | 0.2026 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
