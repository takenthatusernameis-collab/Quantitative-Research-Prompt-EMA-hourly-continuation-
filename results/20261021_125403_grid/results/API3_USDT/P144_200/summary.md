# EMA Hourly Continuation — API3/USDT P144_200

**Symbol:** API3/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.6610 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9015 |
| gross_win_rate | 0.4727 |
| sharpe_ratio | -2.1569 |
| sortino_ratio | -0.4932 |
| max_drawdown | 0.4411 |
| cagr | -0.2034 |
| net_avg_win | 70.1063 |
| net_avg_loss | -95.0686 |
| avg_hold_time_bars | 6.3438 |
| exposure | 0.0738 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
