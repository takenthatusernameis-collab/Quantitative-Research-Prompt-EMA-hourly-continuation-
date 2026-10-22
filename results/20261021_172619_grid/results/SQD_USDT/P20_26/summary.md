# EMA Hourly Continuation — SQD/USDT P20_26

**Symbol:** SQD/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.8144 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0565 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -1.0054 |
| sortino_ratio | -0.2281 |
| max_drawdown | 0.2964 |
| cagr | -0.1002 |
| net_avg_win | 80.0301 |
| net_avg_loss | -104.1483 |
| avg_hold_time_bars | 4.8631 |
| exposure | 0.0551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
