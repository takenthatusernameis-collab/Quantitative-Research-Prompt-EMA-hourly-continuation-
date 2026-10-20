# EMA Hourly Continuation — DGB/USDT P34_55

**Symbol:** DGB/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 999 |
| net_profit_factor | 0.3710 |
| net_win_rate | 0.3994 |
| gross_profit_factor | 0.7974 |
| gross_win_rate | 0.4184 |
| sharpe_ratio | -10.4898 |
| sortino_ratio | -4.7145 |
| max_drawdown | 0.9977 |
| cagr | -0.9098 |
| net_avg_win | 14.7456 |
| net_avg_loss | -26.4329 |
| avg_hold_time_bars | 3.1051 |
| exposure | 0.1410 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
