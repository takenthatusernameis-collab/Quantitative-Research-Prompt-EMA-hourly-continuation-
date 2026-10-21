# EMA Hourly Continuation — PUNDIX/USDT P26_34

**Symbol:** PUNDIX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.5223 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.8684 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -3.7123 |
| sortino_ratio | -0.9881 |
| max_drawdown | 0.6883 |
| cagr | -0.3659 |
| net_avg_win | 46.5703 |
| net_avg_loss | -77.9567 |
| avg_hold_time_bars | 5.1895 |
| exposure | 0.0809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
