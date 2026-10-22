# EMA Hourly Continuation — BICO/USDT P50_200

**Symbol:** BICO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 303 |
| net_profit_factor | 0.7030 |
| net_win_rate | 0.4554 |
| gross_profit_factor | 0.8358 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -1.9295 |
| sortino_ratio | -0.4760 |
| max_drawdown | 0.4349 |
| cagr | -0.1975 |
| net_avg_win | 72.8255 |
| net_avg_loss | -86.6370 |
| avg_hold_time_bars | 31.3366 |
| exposure | 0.4316 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
