# EMA Hourly Continuation — BOME/USDT P50_200

**Symbol:** BOME/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.9436 |
| net_win_rate | 0.5273 |
| gross_profit_factor | 1.1006 |
| gross_win_rate | 0.5273 |
| sharpe_ratio | -0.2326 |
| sortino_ratio | -0.0556 |
| max_drawdown | 0.1877 |
| cagr | -0.0293 |
| net_avg_win | 83.0232 |
| net_avg_loss | -98.1420 |
| avg_hold_time_bars | 33.6109 |
| exposure | 0.4201 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
