# EMA Hourly Continuation — AGLD/USDT P12_50

**Symbol:** AGLD/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 743 |
| net_profit_factor | 0.7335 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9569 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -2.9959 |
| sortino_ratio | -1.1631 |
| max_drawdown | 0.7859 |
| cagr | -0.4141 |
| net_avg_win | 57.0682 |
| net_avg_loss | -71.9613 |
| avg_hold_time_bars | 10.1992 |
| exposure | 0.3429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
