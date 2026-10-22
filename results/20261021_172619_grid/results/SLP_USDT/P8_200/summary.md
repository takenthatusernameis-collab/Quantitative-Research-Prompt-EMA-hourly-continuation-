# EMA Hourly Continuation — SLP/USDT P8_200

**Symbol:** SLP/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7318 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8787 |
| gross_win_rate | 0.4639 |
| sharpe_ratio | -1.9675 |
| sortino_ratio | -0.5297 |
| max_drawdown | 0.4958 |
| cagr | -0.2171 |
| net_avg_win | 75.0277 |
| net_avg_loss | -88.7119 |
| avg_hold_time_bars | 46.7194 |
| exposure | 0.7645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
