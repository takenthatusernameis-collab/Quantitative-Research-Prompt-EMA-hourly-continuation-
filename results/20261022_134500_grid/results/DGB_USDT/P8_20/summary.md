# EMA Hourly Continuation — DGB/USDT P8_20

**Symbol:** DGB/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1815 |
| net_profit_factor | 0.3648 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.9099 |
| gross_win_rate | 0.4204 |
| sharpe_ratio | -14.5181 |
| sortino_ratio | -8.7530 |
| max_drawdown | 1.0000 |
| cagr | -0.9892 |
| net_avg_win | 7.9114 |
| net_avg_loss | -14.4569 |
| avg_hold_time_bars | 2.7091 |
| exposure | 0.2235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
