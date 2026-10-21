# EMA Hourly Continuation — AR/USDT P144_200

**Symbol:** AR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 190 |
| net_profit_factor | 0.7251 |
| net_win_rate | 0.4789 |
| gross_profit_factor | 0.9318 |
| gross_win_rate | 0.4789 |
| sharpe_ratio | -1.4753 |
| sortino_ratio | -0.2904 |
| max_drawdown | 0.3317 |
| cagr | -0.1252 |
| net_avg_win | 82.7107 |
| net_avg_loss | -104.8473 |
| avg_hold_time_bars | 6.7684 |
| exposure | 0.0585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
