# EMA Hourly Continuation — OGN/USDT P100_200

**Symbol:** OGN/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.4298 |
| net_win_rate | 0.4167 |
| gross_profit_factor | 0.7192 |
| gross_win_rate | 0.4324 |
| sharpe_ratio | -5.0176 |
| sortino_ratio | -1.4767 |
| max_drawdown | 0.8472 |
| cagr | -0.5130 |
| net_avg_win | 34.1093 |
| net_avg_loss | -56.6855 |
| avg_hold_time_bars | 9.3086 |
| exposure | 0.1870 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
