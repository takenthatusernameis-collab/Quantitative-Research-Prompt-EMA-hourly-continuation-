# EMA Hourly Continuation — ADA/USDT P12_50

**Symbol:** ADA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1069 |
| net_profit_factor | 0.5165 |
| net_win_rate | 0.4602 |
| gross_profit_factor | 0.9358 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -6.8523 |
| sortino_ratio | -3.1574 |
| max_drawdown | 0.9791 |
| cagr | -0.7835 |
| net_avg_win | 21.2432 |
| net_avg_loss | -35.0732 |
| avg_hold_time_bars | 6.9233 |
| exposure | 0.3364 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
