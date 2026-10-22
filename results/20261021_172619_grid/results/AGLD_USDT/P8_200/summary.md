# EMA Hourly Continuation — AGLD/USDT P8_200

**Symbol:** AGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 349 |
| net_profit_factor | 0.7601 |
| net_win_rate | 0.4670 |
| gross_profit_factor | 0.8977 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -1.7560 |
| sortino_ratio | -0.4647 |
| max_drawdown | 0.4963 |
| cagr | -0.1927 |
| net_avg_win | 81.1108 |
| net_avg_loss | -93.5164 |
| avg_hold_time_bars | 48.5158 |
| exposure | 0.7663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
