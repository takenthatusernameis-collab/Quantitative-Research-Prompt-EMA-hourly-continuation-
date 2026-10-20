# EMA Hourly Continuation — DUSK/USDT P26_89

**Symbol:** DUSK/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.6241 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.8979 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -4.0629 |
| sortino_ratio | -1.4893 |
| max_drawdown | 0.8366 |
| cagr | -0.5068 |
| net_avg_win | 44.1924 |
| net_avg_loss | -60.5294 |
| avg_hold_time_bars | 10.0783 |
| exposure | 0.3101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
