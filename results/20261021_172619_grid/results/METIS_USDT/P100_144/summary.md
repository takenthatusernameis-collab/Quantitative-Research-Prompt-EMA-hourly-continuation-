# EMA Hourly Continuation — METIS/USDT P100_144

**Symbol:** METIS/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 0.6835 |
| net_win_rate | 0.4767 |
| gross_profit_factor | 0.9171 |
| gross_win_rate | 0.4767 |
| sharpe_ratio | -1.9676 |
| sortino_ratio | -0.4518 |
| max_drawdown | 0.4164 |
| cagr | -0.1873 |
| net_avg_win | 71.2735 |
| net_avg_loss | -95.0138 |
| avg_hold_time_bars | 6.9109 |
| exposure | 0.0810 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
