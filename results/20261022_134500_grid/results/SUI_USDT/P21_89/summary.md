# EMA Hourly Continuation — SUI/USDT P21_89

**Symbol:** SUI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.5592 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8966 |
| gross_win_rate | 0.4657 |
| sharpe_ratio | -5.5746 |
| sortino_ratio | -2.1107 |
| max_drawdown | 0.9349 |
| cagr | -0.6537 |
| net_avg_win | 35.2281 |
| net_avg_loss | -51.7255 |
| avg_hold_time_bars | 10.3742 |
| exposure | 0.3504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
