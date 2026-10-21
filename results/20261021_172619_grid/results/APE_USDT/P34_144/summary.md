# EMA Hourly Continuation — APE/USDT P34_144

**Symbol:** APE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.7788 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 0.9506 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -1.3154 |
| sortino_ratio | -0.3401 |
| max_drawdown | 0.3409 |
| cagr | -0.1458 |
| net_avg_win | 71.4648 |
| net_avg_loss | -88.9970 |
| avg_hold_time_bars | 29.3761 |
| exposure | 0.4366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
