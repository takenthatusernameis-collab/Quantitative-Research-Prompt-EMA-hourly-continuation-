# EMA Hourly Continuation — GMX/USDT P20_200

**Symbol:** GMX/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.7892 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9535 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -1.6517 |
| sortino_ratio | -0.4627 |
| max_drawdown | 0.5307 |
| cagr | -0.1927 |
| net_avg_win | 83.2528 |
| net_avg_loss | -98.1420 |
| avg_hold_time_bars | 32.8582 |
| exposure | 0.5795 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
