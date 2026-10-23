# EMA Hourly Continuation — DEGEN/USDT P8_26

**Symbol:** DEGEN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1448 |
| net_profit_factor | 0.6179 |
| net_win_rate | 0.4427 |
| gross_profit_factor | 0.9127 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -8.1350 |
| sortino_ratio | -4.3488 |
| max_drawdown | 0.9951 |
| cagr | -0.8788 |
| net_avg_win | 25.1037 |
| net_avg_loss | -32.2691 |
| avg_hold_time_bars | 4.3854 |
| exposure | 0.2891 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
