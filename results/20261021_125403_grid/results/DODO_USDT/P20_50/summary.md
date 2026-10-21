# EMA Hourly Continuation — DODO/USDT P20_50

**Symbol:** DODO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 584 |
| net_profit_factor | 0.6988 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9352 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -2.9826 |
| sortino_ratio | -1.0271 |
| max_drawdown | 0.7038 |
| cagr | -0.3752 |
| net_avg_win | 57.9636 |
| net_avg_loss | -75.3610 |
| avg_hold_time_bars | 7.5993 |
| exposure | 0.2008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
