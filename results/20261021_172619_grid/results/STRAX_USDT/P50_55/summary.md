# EMA Hourly Continuation — STRAX/USDT P50_55

**Symbol:** STRAX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 236 |
| net_profit_factor | 0.5531 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.9162 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -2.9105 |
| sortino_ratio | -0.6420 |
| max_drawdown | 0.5362 |
| cagr | -0.2569 |
| net_avg_win | 57.8644 |
| net_avg_loss | -94.4902 |
| avg_hold_time_bars | 7.2627 |
| exposure | 0.0784 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
