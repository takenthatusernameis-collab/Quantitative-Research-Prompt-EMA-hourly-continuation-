# EMA Hourly Continuation — BCH/USDT P21_200

**Symbol:** BCH/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 313 |
| net_profit_factor | 0.6354 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 1.0138 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.5533 |
| sortino_ratio | -0.6299 |
| max_drawdown | 0.5735 |
| cagr | -0.2649 |
| net_avg_win | 60.9100 |
| net_avg_loss | -92.8477 |
| avg_hold_time_bars | 47.4920 |
| exposure | 0.6757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
