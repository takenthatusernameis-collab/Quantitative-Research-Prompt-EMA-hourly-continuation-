# EMA Hourly Continuation — AIOZ/USDT P12_20

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 264 |
| net_profit_factor | 0.5564 |
| net_win_rate | 0.4091 |
| gross_profit_factor | 0.7307 |
| gross_win_rate | 0.4091 |
| sharpe_ratio | -3.2644 |
| sortino_ratio | -0.7514 |
| max_drawdown | 0.6004 |
| cagr | -0.2930 |
| net_avg_win | 67.5231 |
| net_avg_loss | -84.0115 |
| avg_hold_time_bars | 5.2614 |
| exposure | 0.0631 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
