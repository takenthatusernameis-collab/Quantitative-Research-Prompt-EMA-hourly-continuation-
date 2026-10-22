# EMA Hourly Continuation — NOT/USDT P20_144

**Symbol:** NOT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.8813 |
| net_win_rate | 0.5088 |
| gross_profit_factor | 1.0391 |
| gross_win_rate | 0.5088 |
| sharpe_ratio | -0.7552 |
| sortino_ratio | -0.2032 |
| max_drawdown | 0.3094 |
| cagr | -0.0920 |
| net_avg_win | 89.7167 |
| net_avg_loss | -105.4569 |
| avg_hold_time_bars | 33.9706 |
| exposure | 0.5426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
