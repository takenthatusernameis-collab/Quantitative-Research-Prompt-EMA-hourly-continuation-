# EMA Hourly Continuation — SLP/USDT P50_89

**Symbol:** SLP/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 416 |
| net_profit_factor | 0.7398 |
| net_win_rate | 0.4976 |
| gross_profit_factor | 1.0057 |
| gross_win_rate | 0.4976 |
| sharpe_ratio | -2.0525 |
| sortino_ratio | -0.6005 |
| max_drawdown | 0.5140 |
| cagr | -0.2417 |
| net_avg_win | 68.7688 |
| net_avg_loss | -92.0711 |
| avg_hold_time_bars | 6.8606 |
| exposure | 0.1297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
