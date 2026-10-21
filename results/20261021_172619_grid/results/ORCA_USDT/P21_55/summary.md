# EMA Hourly Continuation — ORCA/USDT P21_55

**Symbol:** ORCA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 569 |
| net_profit_factor | 0.7771 |
| net_win_rate | 0.5132 |
| gross_profit_factor | 1.0496 |
| gross_win_rate | 0.5132 |
| sharpe_ratio | -1.9486 |
| sortino_ratio | -0.6669 |
| max_drawdown | 0.5684 |
| cagr | -0.2651 |
| net_avg_win | 64.2970 |
| net_avg_loss | -87.2250 |
| avg_hold_time_bars | 8.7381 |
| exposure | 0.2260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
