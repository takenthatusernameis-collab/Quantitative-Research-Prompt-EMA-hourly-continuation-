# EMA Hourly Continuation — HBAR/USDT P12_21

**Symbol:** HBAR/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1519 |
| net_profit_factor | 0.2473 |
| net_win_rate | 0.4167 |
| gross_profit_factor | 0.6960 |
| gross_win_rate | 0.4490 |
| sharpe_ratio | -14.0124 |
| sortino_ratio | -7.8057 |
| max_drawdown | 1.0000 |
| cagr | -0.9836 |
| net_avg_win | 5.1891 |
| net_avg_loss | -14.9936 |
| avg_hold_time_bars | 2.0698 |
| exposure | 0.1429 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
