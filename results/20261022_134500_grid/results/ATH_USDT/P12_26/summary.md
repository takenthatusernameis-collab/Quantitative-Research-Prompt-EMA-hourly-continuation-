# EMA Hourly Continuation — ATH/USDT P12_26

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1297 |
| net_profit_factor | 0.4255 |
| net_win_rate | 0.4333 |
| gross_profit_factor | 0.7973 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -10.0864 |
| sortino_ratio | -5.2799 |
| max_drawdown | 0.9981 |
| cagr | -0.9293 |
| net_avg_win | 13.1528 |
| net_avg_loss | -23.6358 |
| avg_hold_time_bars | 2.8473 |
| exposure | 0.1790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
