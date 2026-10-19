# EMA Hourly Continuation — LINK/USDT P21_26

**Symbol:** LINK/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1129 |
| net_profit_factor | 0.1508 |
| net_win_rate | 0.3171 |
| gross_profit_factor | 0.5833 |
| gross_win_rate | 0.3676 |
| sharpe_ratio | -16.3539 |
| sortino_ratio | -8.2290 |
| max_drawdown | 1.0000 |
| cagr | -0.9893 |
| net_avg_win | 4.9601 |
| net_avg_loss | -15.2731 |
| avg_hold_time_bars | 1.9035 |
| exposure | 0.0977 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
