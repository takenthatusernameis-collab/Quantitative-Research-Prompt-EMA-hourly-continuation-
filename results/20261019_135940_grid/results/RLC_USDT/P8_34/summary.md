# EMA Hourly Continuation — RLC/USDT P8_34

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1315 |
| net_profit_factor | 0.6067 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 1.0265 |
| gross_win_rate | 0.4905 |
| sharpe_ratio | -6.8191 |
| sortino_ratio | -3.4744 |
| max_drawdown | 0.9864 |
| cagr | -0.8143 |
| net_avg_win | 24.3574 |
| net_avg_loss | -36.2565 |
| avg_hold_time_bars | 5.8213 |
| exposure | 0.3480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
