# EMA Hourly Continuation — W/USDT P20_21

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1245 |
| net_profit_factor | 0.2137 |
| net_win_rate | 0.3406 |
| gross_profit_factor | 0.7009 |
| gross_win_rate | 0.4016 |
| sharpe_ratio | -16.0224 |
| sortino_ratio | -8.3276 |
| max_drawdown | 1.0000 |
| cagr | -0.9905 |
| net_avg_win | 6.4084 |
| net_avg_loss | -15.4897 |
| avg_hold_time_bars | 1.7020 |
| exposure | 0.0963 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
