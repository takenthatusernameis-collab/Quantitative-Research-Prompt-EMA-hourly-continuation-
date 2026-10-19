# EMA Hourly Continuation — JST/USDT P20_34

**Symbol:** JST/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 927 |
| net_profit_factor | 0.1249 |
| net_win_rate | 0.3625 |
| gross_profit_factor | 0.7757 |
| gross_win_rate | 0.4714 |
| sharpe_ratio | -12.7359 |
| sortino_ratio | -5.6720 |
| max_drawdown | 0.9995 |
| cagr | -0.9517 |
| net_avg_win | 4.2439 |
| net_avg_loss | -19.3252 |
| avg_hold_time_bars | 3.4552 |
| exposure | 0.1449 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
