# EMA Hourly Continuation — VET/USDT P34_50

**Symbol:** VET/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 240 |
| net_profit_factor | 0.6459 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9708 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.0046 |
| sortino_ratio | -0.4461 |
| max_drawdown | 0.4107 |
| cagr | -0.1840 |
| net_avg_win | 61.2889 |
| net_avg_loss | -93.3222 |
| avg_hold_time_bars | 4.8667 |
| exposure | 0.0531 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
