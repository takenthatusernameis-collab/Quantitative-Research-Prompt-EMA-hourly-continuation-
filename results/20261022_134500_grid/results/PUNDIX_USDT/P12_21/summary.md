# EMA Hourly Continuation — PUNDIX/USDT P12_21

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1372 |
| net_profit_factor | 0.2527 |
| net_win_rate | 0.3827 |
| gross_profit_factor | 0.6605 |
| gross_win_rate | 0.4278 |
| sharpe_ratio | -13.6342 |
| sortino_ratio | -7.2709 |
| max_drawdown | 0.9999 |
| cagr | -0.9753 |
| net_avg_win | 6.4394 |
| net_avg_loss | -15.7967 |
| avg_hold_time_bars | 3.3251 |
| exposure | 0.2074 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
