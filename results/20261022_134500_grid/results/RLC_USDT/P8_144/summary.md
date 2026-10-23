# EMA Hourly Continuation — RLC/USDT P8_144

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7536 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 1.0275 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -2.1914 |
| sortino_ratio | -0.6807 |
| max_drawdown | 0.6363 |
| cagr | -0.2733 |
| net_avg_win | 71.1734 |
| net_avg_loss | -92.8733 |
| avg_hold_time_bars | 34.6444 |
| exposure | 0.7527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
