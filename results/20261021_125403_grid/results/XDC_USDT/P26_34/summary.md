# EMA Hourly Continuation — XDC/USDT P26_34

**Symbol:** XDC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 184 |
| net_profit_factor | 0.5787 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9726 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.1584 |
| sortino_ratio | -0.4230 |
| max_drawdown | 0.3894 |
| cagr | -0.1745 |
| net_avg_win | 57.0692 |
| net_avg_loss | -98.6155 |
| avg_hold_time_bars | 6.0924 |
| exposure | 0.0510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
