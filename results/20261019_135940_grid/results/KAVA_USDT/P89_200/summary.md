# EMA Hourly Continuation — KAVA/USDT P89_200

**Symbol:** KAVA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 434 |
| net_profit_factor | 0.5325 |
| net_win_rate | 0.4585 |
| gross_profit_factor | 0.9446 |
| gross_win_rate | 0.4885 |
| sharpe_ratio | -4.3562 |
| sortino_ratio | -1.2762 |
| max_drawdown | 0.7976 |
| cagr | -0.4661 |
| net_avg_win | 45.4077 |
| net_avg_loss | -72.2061 |
| avg_hold_time_bars | 11.2880 |
| exposure | 0.2227 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
