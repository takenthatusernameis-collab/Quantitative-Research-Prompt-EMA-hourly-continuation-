# EMA Hourly Continuation — EWT/USDT P8_200

**Symbol:** EWT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.5265 |
| net_win_rate | 0.4253 |
| gross_profit_factor | 0.7502 |
| gross_win_rate | 0.4271 |
| sharpe_ratio | -4.8527 |
| sortino_ratio | -1.6003 |
| max_drawdown | 0.8818 |
| cagr | -0.5492 |
| net_avg_win | 39.7305 |
| net_avg_loss | -55.8495 |
| avg_hold_time_bars | 25.8682 |
| exposure | 0.6690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
