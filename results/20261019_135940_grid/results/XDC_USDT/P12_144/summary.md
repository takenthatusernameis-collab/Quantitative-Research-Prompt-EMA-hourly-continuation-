# EMA Hourly Continuation — XDC/USDT P12_144

**Symbol:** XDC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.3726 |
| net_win_rate | 0.4549 |
| gross_profit_factor | 0.7775 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -6.3599 |
| sortino_ratio | -2.3967 |
| max_drawdown | 0.9562 |
| cagr | -0.7107 |
| net_avg_win | 16.7909 |
| net_avg_loss | -37.6080 |
| avg_hold_time_bars | 16.3392 |
| exposure | 0.5518 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
