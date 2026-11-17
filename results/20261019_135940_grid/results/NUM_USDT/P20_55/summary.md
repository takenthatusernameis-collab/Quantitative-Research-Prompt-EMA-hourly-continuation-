# EMA Hourly Continuation — NUM/USDT P20_55

**Symbol:** NUM/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 948 |
| net_profit_factor | 0.3941 |
| net_win_rate | 0.3608 |
| gross_profit_factor | 0.7551 |
| gross_win_rate | 0.3797 |
| sharpe_ratio | -9.8032 |
| sortino_ratio | -4.2626 |
| max_drawdown | 0.9950 |
| cagr | -0.8774 |
| net_avg_win | 18.9198 |
| net_avg_loss | -27.0944 |
| avg_hold_time_bars | 6.2637 |
| exposure | 0.2699 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
