# EMA Hourly Continuation — GALA/USDT P12_34

**Symbol:** GALA/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 563 |
| net_profit_factor | 0.7518 |
| net_win_rate | 0.4902 |
| gross_profit_factor | 0.9862 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -2.3580 |
| sortino_ratio | -0.8012 |
| max_drawdown | 0.6156 |
| cagr | -0.3074 |
| net_avg_win | 66.1262 |
| net_avg_loss | -84.5826 |
| avg_hold_time_bars | 6.2575 |
| exposure | 0.1601 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
