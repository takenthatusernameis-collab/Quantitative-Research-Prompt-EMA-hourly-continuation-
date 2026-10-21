# EMA Hourly Continuation — TRX/USDT P20_21

**Symbol:** TRX/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 90 |
| net_profit_factor | 0.3804 |
| net_win_rate | 0.4889 |
| gross_profit_factor | 0.9982 |
| gross_win_rate | 0.4889 |
| sharpe_ratio | -2.7274 |
| sortino_ratio | -0.3832 |
| max_drawdown | 0.3723 |
| cagr | -0.1649 |
| net_avg_win | 50.7896 |
| net_avg_loss | -127.7230 |
| avg_hold_time_bars | 9.6556 |
| exposure | 0.0395 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
