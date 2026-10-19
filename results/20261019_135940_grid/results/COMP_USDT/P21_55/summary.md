# EMA Hourly Continuation — COMP/USDT P21_55

**Symbol:** COMP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1022 |
| net_profit_factor | 0.4160 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.8298 |
| gross_win_rate | 0.4971 |
| sharpe_ratio | -6.8151 |
| sortino_ratio | -3.0779 |
| max_drawdown | 0.9779 |
| cagr | -0.7760 |
| net_avg_win | 14.3176 |
| net_avg_loss | -31.2033 |
| avg_hold_time_bars | 5.7613 |
| exposure | 0.2676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
