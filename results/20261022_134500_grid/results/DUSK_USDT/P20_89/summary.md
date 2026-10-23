# EMA Hourly Continuation — DUSK/USDT P20_89

**Symbol:** DUSK/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6404 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.9001 |
| gross_win_rate | 0.4562 |
| sharpe_ratio | -4.2095 |
| sortino_ratio | -1.5941 |
| max_drawdown | 0.8530 |
| cagr | -0.5259 |
| net_avg_win | 46.3932 |
| net_avg_loss | -59.7533 |
| avg_hold_time_bars | 11.1238 |
| exposure | 0.3635 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
