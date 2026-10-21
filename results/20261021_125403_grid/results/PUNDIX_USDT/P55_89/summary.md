# EMA Hourly Continuation — PUNDIX/USDT P55_89

**Symbol:** PUNDIX/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.5845 |
| net_win_rate | 0.4783 |
| gross_profit_factor | 0.9026 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -3.1841 |
| sortino_ratio | -0.9033 |
| max_drawdown | 0.6488 |
| cagr | -0.3383 |
| net_avg_win | 48.5707 |
| net_avg_loss | -76.1667 |
| avg_hold_time_bars | 8.1816 |
| exposure | 0.1454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
