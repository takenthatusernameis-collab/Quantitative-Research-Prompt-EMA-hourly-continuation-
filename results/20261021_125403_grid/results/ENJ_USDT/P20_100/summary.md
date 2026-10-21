# EMA Hourly Continuation — ENJ/USDT P20_100

**Symbol:** ENJ/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.7643 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9613 |
| gross_win_rate | 0.4883 |
| sharpe_ratio | -1.9379 |
| sortino_ratio | -0.5989 |
| max_drawdown | 0.5487 |
| cagr | -0.2409 |
| net_avg_win | 70.9586 |
| net_avg_loss | -87.8532 |
| avg_hold_time_bars | 19.1274 |
| exposure | 0.4077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
