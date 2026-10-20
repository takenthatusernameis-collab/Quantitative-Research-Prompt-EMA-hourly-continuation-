# EMA Hourly Continuation — ASTR/USDT P20_200

**Symbol:** ASTR/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.7586 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 1.0286 |
| gross_win_rate | 0.5060 |
| sharpe_ratio | -1.6331 |
| sortino_ratio | -0.4239 |
| max_drawdown | 0.4403 |
| cagr | -0.1805 |
| net_avg_win | 74.2547 |
| net_avg_loss | -96.7301 |
| avg_hold_time_bars | 43.8333 |
| exposure | 0.6665 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
