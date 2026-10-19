# EMA Hourly Continuation — ICP/USDT P26_34

**Symbol:** ICP/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1076 |
| net_profit_factor | 0.2534 |
| net_win_rate | 0.3875 |
| gross_profit_factor | 0.7263 |
| gross_win_rate | 0.4349 |
| sharpe_ratio | -12.5043 |
| sortino_ratio | -5.8818 |
| max_drawdown | 0.9996 |
| cagr | -0.9574 |
| net_avg_win | 8.1381 |
| net_avg_loss | -20.3186 |
| avg_hold_time_bars | 1.9647 |
| exposure | 0.0961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
