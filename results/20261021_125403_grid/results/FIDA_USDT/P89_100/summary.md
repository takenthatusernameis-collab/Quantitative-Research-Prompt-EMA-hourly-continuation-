# EMA Hourly Continuation — FIDA/USDT P89_100

**Symbol:** FIDA/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 206 |
| net_profit_factor | 0.4724 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.7141 |
| gross_win_rate | 0.4175 |
| sharpe_ratio | -3.2632 |
| sortino_ratio | -0.6658 |
| max_drawdown | 0.5479 |
| cagr | -0.2673 |
| net_avg_win | 56.6023 |
| net_avg_loss | -85.8683 |
| avg_hold_time_bars | 6.6505 |
| exposure | 0.0620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
