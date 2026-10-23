# EMA Hourly Continuation — LISTA/USDT P100_144

**Symbol:** LISTA/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.5230 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8191 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -4.4887 |
| sortino_ratio | -1.4251 |
| max_drawdown | 0.7978 |
| cagr | -0.4919 |
| net_avg_win | 41.2663 |
| net_avg_loss | -65.2905 |
| avg_hold_time_bars | 4.9871 |
| exposure | 0.1136 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
