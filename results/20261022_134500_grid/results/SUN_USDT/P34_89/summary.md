# EMA Hourly Continuation — SUN/USDT P34_89

**Symbol:** SUN/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 614 |
| net_profit_factor | 0.3126 |
| net_win_rate | 0.3664 |
| gross_profit_factor | 0.7139 |
| gross_win_rate | 0.4104 |
| sharpe_ratio | -9.3129 |
| sortino_ratio | -3.2754 |
| max_drawdown | 0.9886 |
| cagr | -0.8296 |
| net_avg_win | 19.9827 |
| net_avg_loss | -36.9690 |
| avg_hold_time_bars | 9.1205 |
| exposure | 0.2534 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
