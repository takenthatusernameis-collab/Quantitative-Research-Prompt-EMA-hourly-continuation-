# EMA Hourly Continuation — ARB/USDT P34_55

**Symbol:** ARB/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 301 |
| net_profit_factor | 0.8396 |
| net_win_rate | 0.5349 |
| gross_profit_factor | 1.1400 |
| gross_win_rate | 0.5349 |
| sharpe_ratio | -0.8881 |
| sortino_ratio | -0.2229 |
| max_drawdown | 0.2397 |
| cagr | -0.0983 |
| net_avg_win | 74.4050 |
| net_avg_loss | -101.9174 |
| avg_hold_time_bars | 6.4419 |
| exposure | 0.0881 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
