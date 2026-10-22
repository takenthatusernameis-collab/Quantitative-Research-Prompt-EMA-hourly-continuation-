# EMA Hourly Continuation — BLZ/USDT P20_200

**Symbol:** BLZ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.6834 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9107 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -2.2661 |
| sortino_ratio | -0.5503 |
| max_drawdown | 0.5255 |
| cagr | -0.2273 |
| net_avg_win | 74.2535 |
| net_avg_loss | -95.5907 |
| avg_hold_time_bars | 56.8586 |
| exposure | 0.7642 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
