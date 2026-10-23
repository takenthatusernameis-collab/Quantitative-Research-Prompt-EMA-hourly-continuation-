# EMA Hourly Continuation — LUNA/USDT P50_55

**Symbol:** LUNA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 897 |
| net_profit_factor | 0.1708 |
| net_win_rate | 0.3166 |
| gross_profit_factor | 0.6536 |
| gross_win_rate | 0.3835 |
| sharpe_ratio | -14.4878 |
| sortino_ratio | -6.5249 |
| max_drawdown | 0.9999 |
| cagr | -0.9734 |
| net_avg_win | 7.2512 |
| net_avg_loss | -19.6708 |
| avg_hold_time_bars | 1.8774 |
| exposure | 0.0765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
