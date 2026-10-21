# EMA Hourly Continuation — CELO/USDT P8_200

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 300 |
| net_profit_factor | 0.9366 |
| net_win_rate | 0.5267 |
| gross_profit_factor | 1.1009 |
| gross_win_rate | 0.5267 |
| sharpe_ratio | -0.3411 |
| sortino_ratio | -0.0848 |
| max_drawdown | 0.2838 |
| cagr | -0.0424 |
| net_avg_win | 96.8819 |
| net_avg_loss | -115.0915 |
| avg_hold_time_bars | 59.7067 |
| exposure | 0.8105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
