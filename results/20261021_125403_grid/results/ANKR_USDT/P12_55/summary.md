# EMA Hourly Continuation — ANKR/USDT P12_55

**Symbol:** ANKR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.7138 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 0.9449 |
| gross_win_rate | 0.4716 |
| sharpe_ratio | -3.2531 |
| sortino_ratio | -1.1679 |
| max_drawdown | 0.7540 |
| cagr | -0.4159 |
| net_avg_win | 61.7901 |
| net_avg_loss | -77.2643 |
| avg_hold_time_bars | 14.4748 |
| exposure | 0.4171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
