# EMA Hourly Continuation — JTO/USDT P12_200

**Symbol:** JTO/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.8815 |
| net_win_rate | 0.5016 |
| gross_profit_factor | 1.0003 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -0.6451 |
| sortino_ratio | -0.1623 |
| max_drawdown | 0.2770 |
| cagr | -0.0747 |
| net_avg_win | 84.9460 |
| net_avg_loss | -96.9942 |
| avg_hold_time_bars | 52.0971 |
| exposure | 0.7317 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
