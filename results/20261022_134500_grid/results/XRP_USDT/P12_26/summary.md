# EMA Hourly Continuation — XRP/USDT P12_26

**Symbol:** XRP/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1399 |
| net_profit_factor | 0.1901 |
| net_win_rate | 0.3810 |
| gross_profit_factor | 0.7243 |
| gross_win_rate | 0.4375 |
| sharpe_ratio | -14.9550 |
| sortino_ratio | -8.0447 |
| max_drawdown | 1.0000 |
| cagr | -0.9874 |
| net_avg_win | 4.4029 |
| net_avg_loss | -14.2570 |
| avg_hold_time_bars | 2.6633 |
| exposure | 0.1694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
