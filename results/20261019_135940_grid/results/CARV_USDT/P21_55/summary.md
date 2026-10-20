# EMA Hourly Continuation — CARV/USDT P21_55

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.5711 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9915 |
| gross_win_rate | 0.4969 |
| sharpe_ratio | -4.9806 |
| sortino_ratio | -1.9798 |
| max_drawdown | 0.8633 |
| cagr | -0.6167 |
| net_avg_win | 36.8143 |
| net_avg_loss | -59.4725 |
| avg_hold_time_bars | 7.3607 |
| exposure | 0.2676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
