# EMA Hourly Continuation — MEW/USDT P34_144

**Symbol:** MEW/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.7895 |
| net_win_rate | 0.4880 |
| gross_profit_factor | 0.9479 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -1.4154 |
| sortino_ratio | -0.3912 |
| max_drawdown | 0.3859 |
| cagr | -0.1653 |
| net_avg_win | 74.7587 |
| net_avg_loss | -90.2552 |
| avg_hold_time_bars | 21.4640 |
| exposure | 0.3659 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
