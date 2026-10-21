# EMA Hourly Continuation — W/USDT P21_144

**Symbol:** W/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.9095 |
| net_win_rate | 0.5180 |
| gross_profit_factor | 1.0690 |
| gross_win_rate | 0.5180 |
| sharpe_ratio | -0.5798 |
| sortino_ratio | -0.1640 |
| max_drawdown | 0.2805 |
| cagr | -0.0770 |
| net_avg_win | 91.0776 |
| net_avg_loss | -107.6427 |
| avg_hold_time_bars | 30.4665 |
| exposure | 0.5373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
