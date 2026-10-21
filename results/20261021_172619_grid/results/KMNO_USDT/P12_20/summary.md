# EMA Hourly Continuation — KMNO/USDT P12_20

**Symbol:** KMNO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.7575 |
| net_win_rate | 0.5299 |
| gross_profit_factor | 1.1148 |
| gross_win_rate | 0.5328 |
| sharpe_ratio | -1.5364 |
| sortino_ratio | -0.4179 |
| max_drawdown | 0.4127 |
| cagr | -0.1748 |
| net_avg_win | 63.5020 |
| net_avg_loss | -94.5026 |
| avg_hold_time_bars | 4.8632 |
| exposure | 0.0788 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
