# EMA Hourly Continuation — TRX/USDT P8_34

**Symbol:** TRX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 630 |
| net_profit_factor | 0.4807 |
| net_win_rate | 0.4952 |
| gross_profit_factor | 1.0129 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -6.0428 |
| sortino_ratio | -2.2088 |
| max_drawdown | 0.9244 |
| cagr | -0.6397 |
| net_avg_win | 27.3808 |
| net_avg_loss | -55.8891 |
| avg_hold_time_bars | 9.8206 |
| exposure | 0.2812 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
