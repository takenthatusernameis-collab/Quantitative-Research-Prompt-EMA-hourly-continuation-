# EMA Hourly Continuation — JTO/USDT P100_144

**Symbol:** JTO/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.5383 |
| net_win_rate | 0.4098 |
| gross_profit_factor | 0.6921 |
| gross_win_rate | 0.4098 |
| sharpe_ratio | -2.9832 |
| sortino_ratio | -0.6592 |
| max_drawdown | 0.5431 |
| cagr | -0.2626 |
| net_avg_win | 62.3374 |
| net_avg_loss | -80.4145 |
| avg_hold_time_bars | 6.4795 |
| exposure | 0.0719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
