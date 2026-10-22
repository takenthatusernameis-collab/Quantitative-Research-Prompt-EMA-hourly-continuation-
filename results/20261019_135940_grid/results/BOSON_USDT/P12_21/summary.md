# EMA Hourly Continuation — BOSON/USDT P12_21

**Symbol:** BOSON/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1212 |
| net_profit_factor | 0.3950 |
| net_win_rate | 0.4167 |
| gross_profit_factor | 0.8091 |
| gross_win_rate | 0.4373 |
| sharpe_ratio | -9.9706 |
| sortino_ratio | -4.8950 |
| max_drawdown | 0.9978 |
| cagr | -0.9113 |
| net_avg_win | 12.8969 |
| net_avg_loss | -23.3241 |
| avg_hold_time_bars | 3.3416 |
| exposure | 0.1841 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
