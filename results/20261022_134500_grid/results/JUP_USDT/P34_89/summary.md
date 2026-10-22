# EMA Hourly Continuation — JUP/USDT P34_89

**Symbol:** JUP/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 695 |
| net_profit_factor | 0.5886 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9065 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -4.3637 |
| sortino_ratio | -1.6225 |
| max_drawdown | 0.8685 |
| cagr | -0.5401 |
| net_avg_win | 37.0864 |
| net_avg_loss | -57.2912 |
| avg_hold_time_bars | 6.8432 |
| exposure | 0.2162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
