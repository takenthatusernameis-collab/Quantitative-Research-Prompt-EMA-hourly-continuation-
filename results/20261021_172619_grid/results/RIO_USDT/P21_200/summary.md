# EMA Hourly Continuation — RIO/USDT P21_200

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.7911 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.8821 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -1.4786 |
| sortino_ratio | -0.3840 |
| max_drawdown | 0.4594 |
| cagr | -0.1637 |
| net_avg_win | 88.2238 |
| net_avg_loss | -95.9486 |
| avg_hold_time_bars | 38.4535 |
| exposure | 0.5879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
