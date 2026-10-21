# EMA Hourly Continuation — CVX/USDT P50_144

**Symbol:** CVX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 348 |
| net_profit_factor | 0.7460 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9197 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -1.6344 |
| sortino_ratio | -0.4348 |
| max_drawdown | 0.4083 |
| cagr | -0.1816 |
| net_avg_win | 69.1402 |
| net_avg_loss | -86.5011 |
| avg_hold_time_bars | 16.3534 |
| exposure | 0.2587 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
