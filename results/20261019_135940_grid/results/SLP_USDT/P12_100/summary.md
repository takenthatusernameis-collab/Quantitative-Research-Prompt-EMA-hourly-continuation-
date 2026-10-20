# EMA Hourly Continuation — SLP/USDT P12_100

**Symbol:** SLP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 763 |
| net_profit_factor | 0.6429 |
| net_win_rate | 0.4600 |
| gross_profit_factor | 0.9586 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -4.8699 |
| sortino_ratio | -1.8864 |
| max_drawdown | 0.9039 |
| cagr | -0.5988 |
| net_avg_win | 46.1161 |
| net_avg_loss | -61.1109 |
| avg_hold_time_bars | 16.5229 |
| exposure | 0.5730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
