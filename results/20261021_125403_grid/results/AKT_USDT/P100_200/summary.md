# EMA Hourly Continuation — AKT/USDT P100_200

**Symbol:** AKT/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.8183 |
| net_win_rate | 0.5020 |
| gross_profit_factor | 1.0073 |
| gross_win_rate | 0.5020 |
| sharpe_ratio | -1.0085 |
| sortino_ratio | -0.2308 |
| max_drawdown | 0.2533 |
| cagr | -0.1018 |
| net_avg_win | 83.1345 |
| net_avg_loss | -102.3950 |
| avg_hold_time_bars | 13.1608 |
| exposure | 0.1525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
