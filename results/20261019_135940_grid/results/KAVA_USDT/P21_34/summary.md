# EMA Hourly Continuation — KAVA/USDT P21_34

**Symbol:** KAVA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1191 |
| net_profit_factor | 0.3370 |
| net_win_rate | 0.3770 |
| gross_profit_factor | 0.8457 |
| gross_win_rate | 0.4291 |
| sharpe_ratio | -13.3865 |
| sortino_ratio | -6.6699 |
| max_drawdown | 0.9998 |
| cagr | -0.9698 |
| net_avg_win | 11.3200 |
| net_avg_loss | -20.3250 |
| avg_hold_time_bars | 3.2746 |
| exposure | 0.1773 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
