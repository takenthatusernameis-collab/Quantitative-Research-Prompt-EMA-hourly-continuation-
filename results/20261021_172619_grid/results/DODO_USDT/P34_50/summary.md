# EMA Hourly Continuation — DODO/USDT P34_50

**Symbol:** DODO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.6443 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9139 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -2.5005 |
| sortino_ratio | -0.6574 |
| max_drawdown | 0.5481 |
| cagr | -0.2589 |
| net_avg_win | 59.3147 |
| net_avg_loss | -84.7312 |
| avg_hold_time_bars | 4.8491 |
| exposure | 0.0742 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
