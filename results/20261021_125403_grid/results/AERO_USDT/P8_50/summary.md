# EMA Hourly Continuation — AERO/USDT P8_50

**Symbol:** AERO/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.9030 |
| net_win_rate | 0.5209 |
| gross_profit_factor | 1.0871 |
| gross_win_rate | 0.5209 |
| sharpe_ratio | -0.8969 |
| sortino_ratio | -0.3338 |
| max_drawdown | 0.5039 |
| cagr | -0.1479 |
| net_avg_win | 88.2838 |
| net_avg_loss | -106.2924 |
| avg_hold_time_bars | 13.9881 |
| exposure | 0.4260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
