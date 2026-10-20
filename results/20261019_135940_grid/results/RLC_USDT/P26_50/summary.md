# EMA Hourly Continuation — RLC/USDT P26_50

**Symbol:** RLC/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 931 |
| net_profit_factor | 0.4820 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.9344 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -7.0444 |
| sortino_ratio | -3.0317 |
| max_drawdown | 0.9775 |
| cagr | -0.7741 |
| net_avg_win | 20.9740 |
| net_avg_loss | -37.8377 |
| avg_hold_time_bars | 3.8507 |
| exposure | 0.1630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
