# EMA Hourly Continuation — OSMO/USDT P21_34

**Symbol:** OSMO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.5382 |
| net_win_rate | 0.4120 |
| gross_profit_factor | 0.8240 |
| gross_win_rate | 0.4120 |
| sharpe_ratio | -4.9213 |
| sortino_ratio | -1.4622 |
| max_drawdown | 0.8205 |
| cagr | -0.4907 |
| net_avg_win | 53.4532 |
| net_avg_loss | -69.5976 |
| avg_hold_time_bars | 4.9398 |
| exposure | 0.0970 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
