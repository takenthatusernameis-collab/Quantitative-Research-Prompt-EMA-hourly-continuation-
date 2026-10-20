# EMA Hourly Continuation — MOVR/USDT P89_144

**Symbol:** MOVR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 519 |
| net_profit_factor | 0.5155 |
| net_win_rate | 0.4509 |
| gross_profit_factor | 0.8891 |
| gross_win_rate | 0.4624 |
| sharpe_ratio | -4.5857 |
| sortino_ratio | -1.4708 |
| max_drawdown | 0.8332 |
| cagr | -0.5080 |
| net_avg_win | 37.8076 |
| net_avg_loss | -60.2192 |
| avg_hold_time_bars | 5.8054 |
| exposure | 0.1370 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
