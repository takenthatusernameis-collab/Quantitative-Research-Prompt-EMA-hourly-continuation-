# EMA Hourly Continuation — CELO/USDT P8_50

**Symbol:** CELO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1050 |
| net_profit_factor | 0.6089 |
| net_win_rate | 0.4705 |
| gross_profit_factor | 0.9647 |
| gross_win_rate | 0.4819 |
| sharpe_ratio | -5.3622 |
| sortino_ratio | -2.4480 |
| max_drawdown | 0.9478 |
| cagr | -0.6881 |
| net_avg_win | 29.8501 |
| net_avg_loss | -43.5550 |
| avg_hold_time_bars | 10.1086 |
| exposure | 0.4803 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
