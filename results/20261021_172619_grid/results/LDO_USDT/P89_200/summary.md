# EMA Hourly Continuation — LDO/USDT P89_200

**Symbol:** LDO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 270 |
| net_profit_factor | 0.6024 |
| net_win_rate | 0.4407 |
| gross_profit_factor | 0.7451 |
| gross_win_rate | 0.4407 |
| sharpe_ratio | -2.3577 |
| sortino_ratio | -0.5481 |
| max_drawdown | 0.4977 |
| cagr | -0.2231 |
| net_avg_win | 59.7789 |
| net_avg_loss | -78.1986 |
| avg_hold_time_bars | 16.2370 |
| exposure | 0.1993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
