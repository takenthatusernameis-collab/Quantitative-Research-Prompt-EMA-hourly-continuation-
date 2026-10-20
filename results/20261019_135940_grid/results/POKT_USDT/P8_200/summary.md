# EMA Hourly Continuation — POKT/USDT P8_200

**Symbol:** POKT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.5907 |
| net_win_rate | 0.4161 |
| gross_profit_factor | 0.8297 |
| gross_win_rate | 0.4239 |
| sharpe_ratio | -5.1366 |
| sortino_ratio | -1.8102 |
| max_drawdown | 0.8956 |
| cagr | -0.5835 |
| net_avg_win | 47.9449 |
| net_avg_loss | -57.8493 |
| avg_hold_time_bars | 24.8385 |
| exposure | 0.7239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
