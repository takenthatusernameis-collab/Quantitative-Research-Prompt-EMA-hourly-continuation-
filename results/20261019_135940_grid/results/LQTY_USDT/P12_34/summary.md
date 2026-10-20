# EMA Hourly Continuation — LQTY/USDT P12_34

**Symbol:** LQTY/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1249 |
| net_profit_factor | 0.4535 |
| net_win_rate | 0.4572 |
| gross_profit_factor | 0.8078 |
| gross_win_rate | 0.4684 |
| sharpe_ratio | -7.8881 |
| sortino_ratio | -3.9142 |
| max_drawdown | 0.9921 |
| cagr | -0.8526 |
| net_avg_win | 14.4175 |
| net_avg_loss | -26.7736 |
| avg_hold_time_bars | 4.9504 |
| exposure | 0.2798 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
