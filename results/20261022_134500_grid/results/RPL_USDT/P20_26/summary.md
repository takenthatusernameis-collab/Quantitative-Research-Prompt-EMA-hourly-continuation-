# EMA Hourly Continuation — RPL/USDT P20_26

**Symbol:** RPL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1097 |
| net_profit_factor | 0.2892 |
| net_win_rate | 0.4057 |
| gross_profit_factor | 0.8170 |
| gross_win_rate | 0.4458 |
| sharpe_ratio | -11.1412 |
| sortino_ratio | -5.2566 |
| max_drawdown | 0.9988 |
| cagr | -0.9315 |
| net_avg_win | 9.1338 |
| net_avg_loss | -21.5537 |
| avg_hold_time_bars | 2.9827 |
| exposure | 0.1481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
