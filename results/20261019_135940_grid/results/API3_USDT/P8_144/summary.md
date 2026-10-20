# EMA Hourly Continuation — API3/USDT P8_144

**Symbol:** API3/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 576 |
| net_profit_factor | 0.6917 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9546 |
| gross_win_rate | 0.4792 |
| sharpe_ratio | -3.1214 |
| sortino_ratio | -1.0526 |
| max_drawdown | 0.7224 |
| cagr | -0.3937 |
| net_avg_win | 59.0046 |
| net_avg_loss | -76.3261 |
| avg_hold_time_bars | 27.4774 |
| exposure | 0.7194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
