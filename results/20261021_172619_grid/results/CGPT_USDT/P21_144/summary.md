# EMA Hourly Continuation — CGPT/USDT P21_144

**Symbol:** CGPT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.8965 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0592 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -0.6580 |
| sortino_ratio | -0.1794 |
| max_drawdown | 0.2861 |
| cagr | -0.0825 |
| net_avg_win | 90.9855 |
| net_avg_loss | -107.2919 |
| avg_hold_time_bars | 31.3806 |
| exposure | 0.5135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
