# EMA Hourly Continuation — EWT/USDT P20_34

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1009 |
| net_profit_factor | 0.3427 |
| net_win_rate | 0.3617 |
| gross_profit_factor | 0.6976 |
| gross_win_rate | 0.3865 |
| sharpe_ratio | -11.9940 |
| sortino_ratio | -5.4359 |
| max_drawdown | 0.9992 |
| cagr | -0.9417 |
| net_avg_win | 14.2750 |
| net_avg_loss | -23.6062 |
| avg_hold_time_bars | 3.3449 |
| exposure | 0.1534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
