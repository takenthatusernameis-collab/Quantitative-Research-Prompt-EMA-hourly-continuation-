# EMA Hourly Continuation — ARPA/USDT P50_55

**Symbol:** ARPA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 894 |
| net_profit_factor | 0.2087 |
| net_win_rate | 0.3333 |
| gross_profit_factor | 0.7594 |
| gross_win_rate | 0.4251 |
| sharpe_ratio | -13.3047 |
| sortino_ratio | -5.8822 |
| max_drawdown | 0.9996 |
| cagr | -0.9549 |
| net_avg_win | 8.8445 |
| net_avg_loss | -21.1940 |
| avg_hold_time_bars | 2.5213 |
| exposure | 0.1020 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
