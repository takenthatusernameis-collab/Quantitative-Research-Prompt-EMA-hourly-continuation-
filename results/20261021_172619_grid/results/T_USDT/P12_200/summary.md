# EMA Hourly Continuation — T/USDT P12_200

**Symbol:** T/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 225 |
| net_profit_factor | 0.9175 |
| net_win_rate | 0.5378 |
| gross_profit_factor | 1.1530 |
| gross_win_rate | 0.5378 |
| sharpe_ratio | -0.3464 |
| sortino_ratio | -0.0747 |
| max_drawdown | 0.2656 |
| cagr | -0.0366 |
| net_avg_win | 82.5913 |
| net_avg_loss | -104.7321 |
| avg_hold_time_bars | 77.9022 |
| exposure | 0.7932 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
