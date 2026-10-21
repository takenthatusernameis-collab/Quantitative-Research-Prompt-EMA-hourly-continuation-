# EMA Hourly Continuation — TURBO/USDT P8_200

**Symbol:** TURBO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 273 |
| net_profit_factor | 0.7485 |
| net_win_rate | 0.4615 |
| gross_profit_factor | 0.8654 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -1.7748 |
| sortino_ratio | -0.4548 |
| max_drawdown | 0.4166 |
| cagr | -0.1896 |
| net_avg_win | 84.0381 |
| net_avg_loss | -96.2390 |
| avg_hold_time_bars | 50.3370 |
| exposure | 0.7497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
