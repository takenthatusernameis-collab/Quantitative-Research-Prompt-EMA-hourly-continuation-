# EMA Hourly Continuation — AR/USDT P8_12

**Symbol:** AR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 221 |
| net_profit_factor | 0.7068 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 0.9624 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -1.6603 |
| sortino_ratio | -0.3535 |
| max_drawdown | 0.3335 |
| cagr | -0.1492 |
| net_avg_win | 74.4336 |
| net_avg_loss | -100.6535 |
| avg_hold_time_bars | 5.0995 |
| exposure | 0.0512 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
