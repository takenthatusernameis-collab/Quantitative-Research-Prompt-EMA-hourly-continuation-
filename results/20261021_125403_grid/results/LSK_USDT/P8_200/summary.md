# EMA Hourly Continuation — LSK/USDT P8_200

**Symbol:** LSK/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.8981 |
| net_win_rate | 0.5273 |
| gross_profit_factor | 1.1099 |
| gross_win_rate | 0.5273 |
| sharpe_ratio | -0.6358 |
| sortino_ratio | -0.1660 |
| max_drawdown | 0.3789 |
| cagr | -0.0767 |
| net_avg_win | 91.9196 |
| net_avg_loss | -114.1636 |
| avg_hold_time_bars | 52.1000 |
| exposure | 0.7815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
