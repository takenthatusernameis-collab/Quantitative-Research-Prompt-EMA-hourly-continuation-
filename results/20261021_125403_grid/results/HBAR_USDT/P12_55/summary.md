# EMA Hourly Continuation — HBAR/USDT P12_55

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.8379 |
| net_win_rate | 0.5246 |
| gross_profit_factor | 1.1042 |
| gross_win_rate | 0.5246 |
| sharpe_ratio | -1.4961 |
| sortino_ratio | -0.5418 |
| max_drawdown | 0.5284 |
| cagr | -0.2213 |
| net_avg_win | 72.8033 |
| net_avg_loss | -95.8717 |
| avg_hold_time_bars | 10.8590 |
| exposure | 0.3115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
