# EMA Hourly Continuation — RIO/USDT P55_200

**Symbol:** RIO/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.7542 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8551 |
| gross_win_rate | 0.4618 |
| sharpe_ratio | -1.5768 |
| sortino_ratio | -0.3982 |
| max_drawdown | 0.4343 |
| cagr | -0.1689 |
| net_avg_win | 78.0240 |
| net_avg_loss | -88.7584 |
| avg_hold_time_bars | 21.4586 |
| exposure | 0.3093 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
