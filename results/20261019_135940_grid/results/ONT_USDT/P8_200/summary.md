# EMA Hourly Continuation — ONT/USDT P8_200

**Symbol:** ONT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.5649 |
| net_win_rate | 0.4274 |
| gross_profit_factor | 0.8325 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -4.0524 |
| sortino_ratio | -1.2335 |
| max_drawdown | 0.7822 |
| cagr | -0.4465 |
| net_avg_win | 49.5628 |
| net_avg_loss | -65.4853 |
| avg_hold_time_bars | 35.0989 |
| exposure | 0.7544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
