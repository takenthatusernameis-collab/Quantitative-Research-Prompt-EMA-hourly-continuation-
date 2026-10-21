# EMA Hourly Continuation — KSM/USDT P20_21

**Symbol:** KSM/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 170 |
| net_profit_factor | 0.4835 |
| net_win_rate | 0.4118 |
| gross_profit_factor | 0.7353 |
| gross_win_rate | 0.4118 |
| sharpe_ratio | -3.1033 |
| sortino_ratio | -0.5793 |
| max_drawdown | 0.4994 |
| cagr | -0.2350 |
| net_avg_win | 65.4840 |
| net_avg_loss | -94.8093 |
| avg_hold_time_bars | 4.1353 |
| exposure | 0.0320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
