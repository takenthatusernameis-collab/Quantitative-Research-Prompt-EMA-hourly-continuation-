# EMA Hourly Continuation — ZRX/USDT P50_89

**Symbol:** ZRX/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 670 |
| net_profit_factor | 0.4682 |
| net_win_rate | 0.4433 |
| gross_profit_factor | 0.8412 |
| gross_win_rate | 0.4612 |
| sharpe_ratio | -6.1854 |
| sortino_ratio | -2.2595 |
| max_drawdown | 0.9388 |
| cagr | -0.6676 |
| net_avg_win | 27.7768 |
| net_avg_loss | -47.2406 |
| avg_hold_time_bars | 5.1657 |
| exposure | 0.1573 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
