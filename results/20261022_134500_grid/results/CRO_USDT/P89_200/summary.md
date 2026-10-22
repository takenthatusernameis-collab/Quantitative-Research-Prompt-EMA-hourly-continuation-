# EMA Hourly Continuation — CRO/USDT P89_200

**Symbol:** CRO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.4090 |
| net_win_rate | 0.4344 |
| gross_profit_factor | 0.7696 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -4.8718 |
| sortino_ratio | -1.3531 |
| max_drawdown | 0.8253 |
| cagr | -0.4914 |
| net_avg_win | 33.4519 |
| net_avg_loss | -62.8297 |
| avg_hold_time_bars | 12.1620 |
| exposure | 0.2150 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
