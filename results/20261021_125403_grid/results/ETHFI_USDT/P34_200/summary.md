# EMA Hourly Continuation — ETHFI/USDT P34_200

**Symbol:** ETHFI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.9595 |
| net_win_rate | 0.5260 |
| gross_profit_factor | 1.1037 |
| gross_win_rate | 0.5260 |
| sharpe_ratio | -0.2001 |
| sortino_ratio | -0.0506 |
| max_drawdown | 0.2314 |
| cagr | -0.0279 |
| net_avg_win | 100.1518 |
| net_avg_loss | -115.8206 |
| avg_hold_time_bars | 35.5325 |
| exposure | 0.4975 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
