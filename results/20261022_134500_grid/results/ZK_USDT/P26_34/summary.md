# EMA Hourly Continuation — ZK/USDT P26_34

**Symbol:** ZK/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1050 |
| net_profit_factor | 0.3985 |
| net_win_rate | 0.4057 |
| gross_profit_factor | 0.8609 |
| gross_win_rate | 0.4343 |
| sharpe_ratio | -10.9650 |
| sortino_ratio | -5.2359 |
| max_drawdown | 0.9981 |
| cagr | -0.9313 |
| net_avg_win | 15.5194 |
| net_avg_loss | -26.5903 |
| avg_hold_time_bars | 2.1905 |
| exposure | 0.1121 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
