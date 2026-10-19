# EMA Hourly Continuation — DOT/USDT P34_144

**Symbol:** DOT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.6313 |
| net_win_rate | 0.4722 |
| gross_profit_factor | 0.9337 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -3.3364 |
| sortino_ratio | -0.9942 |
| max_drawdown | 0.7059 |
| cagr | -0.3807 |
| net_avg_win | 56.5220 |
| net_avg_loss | -80.0873 |
| avg_hold_time_bars | 19.6615 |
| exposure | 0.4013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
