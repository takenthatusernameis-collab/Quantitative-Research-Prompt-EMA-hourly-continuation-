# EMA Hourly Continuation — ORDI/USDT P8_200

**Symbol:** ORDI/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 377 |
| net_profit_factor | 0.7579 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 1.0045 |
| gross_win_rate | 0.4960 |
| sharpe_ratio | -1.9118 |
| sortino_ratio | -0.5257 |
| max_drawdown | 0.5390 |
| cagr | -0.2181 |
| net_avg_win | 77.5591 |
| net_avg_loss | -99.6611 |
| avg_hold_time_bars | 47.0451 |
| exposure | 0.8062 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
