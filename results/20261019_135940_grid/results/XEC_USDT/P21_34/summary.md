# EMA Hourly Continuation — XEC/USDT P21_34

**Symbol:** XEC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1227 |
| net_profit_factor | 0.3326 |
| net_win_rate | 0.4132 |
| gross_profit_factor | 0.8587 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -11.8608 |
| sortino_ratio | -5.9481 |
| max_drawdown | 0.9995 |
| cagr | -0.9511 |
| net_avg_win | 9.8250 |
| net_avg_loss | -20.8004 |
| avg_hold_time_bars | 3.0220 |
| exposure | 0.1678 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
