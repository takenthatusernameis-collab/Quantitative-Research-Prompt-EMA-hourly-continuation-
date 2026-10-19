# EMA Hourly Continuation — SHIB/USDT P20_89

**Symbol:** SHIB/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 734 |
| net_profit_factor | 0.5658 |
| net_win_rate | 0.4605 |
| gross_profit_factor | 0.9332 |
| gross_win_rate | 0.4728 |
| sharpe_ratio | -5.3668 |
| sortino_ratio | -2.0423 |
| max_drawdown | 0.9192 |
| cagr | -0.6296 |
| net_avg_win | 35.3693 |
| net_avg_loss | -53.3560 |
| avg_hold_time_bars | 10.6744 |
| exposure | 0.3561 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
