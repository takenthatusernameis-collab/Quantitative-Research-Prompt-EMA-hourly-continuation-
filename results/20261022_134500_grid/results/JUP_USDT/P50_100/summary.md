# EMA Hourly Continuation — JUP/USDT P50_100

**Symbol:** JUP/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.5022 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.8071 |
| gross_win_rate | 0.4625 |
| sharpe_ratio | -5.0768 |
| sortino_ratio | -1.7761 |
| max_drawdown | 0.8948 |
| cagr | -0.5863 |
| net_avg_win | 31.2138 |
| net_avg_loss | -52.8018 |
| avg_hold_time_bars | 5.3700 |
| exposure | 0.1530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
