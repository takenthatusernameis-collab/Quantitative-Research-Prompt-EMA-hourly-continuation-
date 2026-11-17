# EMA Hourly Continuation — NUM/USDT P8_200

**Symbol:** NUM/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 527 |
| net_profit_factor | 0.6107 |
| net_win_rate | 0.4421 |
| gross_profit_factor | 0.8257 |
| gross_win_rate | 0.4440 |
| sharpe_ratio | -3.7034 |
| sortino_ratio | -1.1893 |
| max_drawdown | 0.7681 |
| cagr | -0.4318 |
| net_avg_win | 51.0364 |
| net_avg_loss | -66.2352 |
| avg_hold_time_bars | 30.3757 |
| exposure | 0.7276 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
