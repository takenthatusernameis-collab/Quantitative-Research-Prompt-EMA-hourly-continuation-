# EMA Hourly Continuation — LPT/USDT P20_21

**Symbol:** LPT/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1300 |
| net_profit_factor | 0.2024 |
| net_win_rate | 0.2969 |
| gross_profit_factor | 0.6766 |
| gross_win_rate | 0.3923 |
| sharpe_ratio | -17.9869 |
| sortino_ratio | -9.7711 |
| max_drawdown | 1.0000 |
| cagr | -0.9956 |
| net_avg_win | 6.5752 |
| net_avg_loss | -13.7177 |
| avg_hold_time_bars | 1.8362 |
| exposure | 0.1085 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
