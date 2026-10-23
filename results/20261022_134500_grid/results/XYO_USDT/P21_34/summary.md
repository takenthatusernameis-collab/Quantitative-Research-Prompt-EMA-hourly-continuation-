# EMA Hourly Continuation — XYO/USDT P21_34

**Symbol:** XYO/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1212 |
| net_profit_factor | 0.2420 |
| net_win_rate | 0.3540 |
| gross_profit_factor | 0.6189 |
| gross_win_rate | 0.3853 |
| sharpe_ratio | -13.9176 |
| sortino_ratio | -7.0066 |
| max_drawdown | 0.9999 |
| cagr | -0.9729 |
| net_avg_win | 7.4431 |
| net_avg_loss | -16.8480 |
| avg_hold_time_bars | 3.0726 |
| exposure | 0.1685 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
