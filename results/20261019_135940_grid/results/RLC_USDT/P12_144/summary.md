# EMA Hourly Continuation — RLC/USDT P12_144

**Symbol:** RLC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7070 |
| net_win_rate | 0.4885 |
| gross_profit_factor | 0.9743 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -2.4762 |
| sortino_ratio | -0.7681 |
| max_drawdown | 0.6202 |
| cagr | -0.3029 |
| net_avg_win | 61.4464 |
| net_avg_loss | -83.0108 |
| avg_hold_time_bars | 31.4656 |
| exposure | 0.6851 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
