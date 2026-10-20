# EMA Hourly Continuation — ZEN/USDT P21_100

**Symbol:** ZEN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 688 |
| net_profit_factor | 0.6020 |
| net_win_rate | 0.4666 |
| gross_profit_factor | 0.9013 |
| gross_win_rate | 0.4738 |
| sharpe_ratio | -4.2355 |
| sortino_ratio | -1.5600 |
| max_drawdown | 0.8536 |
| cagr | -0.5282 |
| net_avg_win | 39.9804 |
| net_avg_loss | -58.0867 |
| avg_hold_time_bars | 12.9724 |
| exposure | 0.4057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
