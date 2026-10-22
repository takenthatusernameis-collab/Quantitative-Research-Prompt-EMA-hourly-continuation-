# EMA Hourly Continuation — TRADE/USDT P34_200

**Symbol:** TRADE/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.6746 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8524 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -2.4199 |
| sortino_ratio | -0.6313 |
| max_drawdown | 0.5611 |
| cagr | -0.2558 |
| net_avg_win | 70.0785 |
| net_avg_loss | -86.5618 |
| avg_hold_time_bars | 28.9091 |
| exposure | 0.4481 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
