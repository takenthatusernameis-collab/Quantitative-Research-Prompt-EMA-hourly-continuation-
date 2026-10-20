# EMA Hourly Continuation — SAFE/USDT P26_55

**Symbol:** SAFE/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 892 |
| net_profit_factor | 0.5434 |
| net_win_rate | 0.4697 |
| gross_profit_factor | 1.0002 |
| gross_win_rate | 0.4798 |
| sharpe_ratio | -6.1917 |
| sortino_ratio | -2.6053 |
| max_drawdown | 0.9612 |
| cagr | -0.7216 |
| net_avg_win | 27.2361 |
| net_avg_loss | -44.3955 |
| avg_hold_time_bars | 4.9922 |
| exposure | 0.2039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
