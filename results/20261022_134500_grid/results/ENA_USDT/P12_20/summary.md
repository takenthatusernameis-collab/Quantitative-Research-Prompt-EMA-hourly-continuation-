# EMA Hourly Continuation — ENA/USDT P12_20

**Symbol:** ENA/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1510 |
| net_profit_factor | 0.3679 |
| net_win_rate | 0.4285 |
| gross_profit_factor | 0.7421 |
| gross_win_rate | 0.4470 |
| sharpe_ratio | -10.9831 |
| sortino_ratio | -6.0473 |
| max_drawdown | 0.9995 |
| cagr | -0.9516 |
| net_avg_win | 8.9925 |
| net_avg_loss | -18.3235 |
| avg_hold_time_bars | 2.0960 |
| exposure | 0.1439 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
