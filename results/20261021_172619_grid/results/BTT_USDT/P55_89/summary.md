# EMA Hourly Continuation — BTT/USDT P55_89

**Symbol:** BTT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.4134 |
| net_win_rate | 0.4202 |
| gross_profit_factor | 0.7596 |
| gross_win_rate | 0.4235 |
| sharpe_ratio | -5.0505 |
| sortino_ratio | -1.2826 |
| max_drawdown | 0.7826 |
| cagr | -0.4536 |
| net_avg_win | 42.6637 |
| net_avg_loss | -74.7862 |
| avg_hold_time_bars | 7.5244 |
| exposure | 0.1050 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
