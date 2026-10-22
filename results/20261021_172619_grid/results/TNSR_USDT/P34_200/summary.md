# EMA Hourly Continuation — TNSR/USDT P34_200

**Symbol:** TNSR/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.8166 |
| net_win_rate | 0.4926 |
| gross_profit_factor | 0.9692 |
| gross_win_rate | 0.4926 |
| sharpe_ratio | -1.1802 |
| sortino_ratio | -0.3088 |
| max_drawdown | 0.3739 |
| cagr | -0.1338 |
| net_avg_win | 81.5138 |
| net_avg_loss | -96.9008 |
| avg_hold_time_bars | 32.8131 |
| exposure | 0.5004 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
