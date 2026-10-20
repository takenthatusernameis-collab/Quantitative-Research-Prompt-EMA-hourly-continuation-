# EMA Hourly Continuation — NMR/USDT P55_100

**Symbol:** NMR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 669 |
| net_profit_factor | 0.5222 |
| net_win_rate | 0.4753 |
| gross_profit_factor | 0.9596 |
| gross_win_rate | 0.4993 |
| sharpe_ratio | -5.4295 |
| sortino_ratio | -1.9697 |
| max_drawdown | 0.9169 |
| cagr | -0.6232 |
| net_avg_win | 31.4085 |
| net_avg_loss | -54.4905 |
| avg_hold_time_bars | 5.1854 |
| exposure | 0.1577 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
