# EMA Hourly Continuation — BNB/USDT P8_34

**Symbol:** BNB/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.5885 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9938 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -4.2052 |
| sortino_ratio | -1.5605 |
| max_drawdown | 0.8362 |
| cagr | -0.5087 |
| net_avg_win | 35.9586 |
| net_avg_loss | -61.0994 |
| avg_hold_time_bars | 8.5438 |
| exposure | 0.2571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
