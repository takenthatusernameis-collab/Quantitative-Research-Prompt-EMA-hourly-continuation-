# EMA Hourly Continuation — RLC/USDT P34_100

**Symbol:** RLC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.5943 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9230 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -4.4188 |
| sortino_ratio | -1.6125 |
| max_drawdown | 0.8685 |
| cagr | -0.5385 |
| net_avg_win | 39.5844 |
| net_avg_loss | -59.8132 |
| avg_hold_time_bars | 9.0582 |
| exposure | 0.2759 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
