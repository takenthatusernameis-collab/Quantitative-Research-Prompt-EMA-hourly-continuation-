# EMA Hourly Continuation — SUPER/USDT P12_55

**Symbol:** SUPER/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.8034 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0177 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -2.0105 |
| sortino_ratio | -0.7441 |
| max_drawdown | 0.6004 |
| cagr | -0.2916 |
| net_avg_win | 70.6827 |
| net_avg_loss | -87.9758 |
| avg_hold_time_bars | 11.3463 |
| exposure | 0.3455 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
