# EMA Hourly Continuation — EWT/USDT P21_55

**Symbol:** EWT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.6495 |
| net_win_rate | 0.4628 |
| gross_profit_factor | 0.8479 |
| gross_win_rate | 0.4628 |
| sharpe_ratio | -2.7841 |
| sortino_ratio | -0.8341 |
| max_drawdown | 0.6220 |
| cagr | -0.3187 |
| net_avg_win | 55.9173 |
| net_avg_loss | -74.1517 |
| avg_hold_time_bars | 8.4582 |
| exposure | 0.1703 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
