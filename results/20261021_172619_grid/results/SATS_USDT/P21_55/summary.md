# EMA Hourly Continuation — SATS/USDT P21_55

**Symbol:** SATS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 537 |
| net_profit_factor | 0.6360 |
| net_win_rate | 0.4376 |
| gross_profit_factor | 0.8277 |
| gross_win_rate | 0.4376 |
| sharpe_ratio | -3.7996 |
| sortino_ratio | -1.2447 |
| max_drawdown | 0.7748 |
| cagr | -0.4385 |
| net_avg_win | 57.0061 |
| net_avg_loss | -69.7502 |
| avg_hold_time_bars | 8.3538 |
| exposure | 0.2030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
