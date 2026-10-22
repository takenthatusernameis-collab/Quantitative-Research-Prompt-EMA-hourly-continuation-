# EMA Hourly Continuation — LINK/USDT P26_50

**Symbol:** LINK/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 897 |
| net_profit_factor | 0.4671 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.8798 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -8.5954 |
| sortino_ratio | -3.6443 |
| max_drawdown | 0.9900 |
| cagr | -0.8394 |
| net_avg_win | 22.3608 |
| net_avg_loss | -36.4927 |
| avg_hold_time_bars | 3.7648 |
| exposure | 0.1535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
