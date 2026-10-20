# EMA Hourly Continuation — DODO/USDT P21_26

**Symbol:** DODO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1254 |
| net_profit_factor | 0.2111 |
| net_win_rate | 0.3453 |
| gross_profit_factor | 0.6672 |
| gross_win_rate | 0.4051 |
| sharpe_ratio | -14.4564 |
| sortino_ratio | -7.3885 |
| max_drawdown | 0.9999 |
| cagr | -0.9790 |
| net_avg_win | 6.1800 |
| net_avg_loss | -15.4389 |
| avg_hold_time_bars | 2.3453 |
| exposure | 0.1331 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
