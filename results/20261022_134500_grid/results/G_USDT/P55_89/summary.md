# EMA Hourly Continuation — G/USDT P55_89

**Symbol:** G/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 517 |
| net_profit_factor | 0.4322 |
| net_win_rate | 0.4526 |
| gross_profit_factor | 0.8277 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -5.6867 |
| sortino_ratio | -1.9829 |
| max_drawdown | 0.8755 |
| cagr | -0.6108 |
| net_avg_win | 28.3339 |
| net_avg_loss | -54.2080 |
| avg_hold_time_bars | 5.2476 |
| exposure | 0.1427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
