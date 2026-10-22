# EMA Hourly Continuation — ZKJ/USDT P50_144

**Symbol:** ZKJ/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.2503 |
| net_win_rate | 0.3545 |
| gross_profit_factor | 0.6322 |
| gross_win_rate | 0.4040 |
| sharpe_ratio | -8.2755 |
| sortino_ratio | -2.6528 |
| max_drawdown | 0.9703 |
| cagr | -0.7483 |
| net_avg_win | 18.0686 |
| net_avg_loss | -39.6361 |
| avg_hold_time_bars | 25.9564 |
| exposure | 0.5958 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
