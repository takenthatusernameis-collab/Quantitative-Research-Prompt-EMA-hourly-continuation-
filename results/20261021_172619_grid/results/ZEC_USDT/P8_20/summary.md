# EMA Hourly Continuation — ZEC/USDT P8_20

**Symbol:** ZEC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.5420 |
| net_win_rate | 0.4371 |
| gross_profit_factor | 0.7112 |
| gross_win_rate | 0.4371 |
| sharpe_ratio | -3.3409 |
| sortino_ratio | -0.9911 |
| max_drawdown | 0.6821 |
| cagr | -0.3664 |
| net_avg_win | 42.2634 |
| net_avg_loss | -60.5429 |
| avg_hold_time_bars | 5.5927 |
| exposure | 0.1111 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
