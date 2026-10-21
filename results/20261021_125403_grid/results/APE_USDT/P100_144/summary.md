# EMA Hourly Continuation — APE/USDT P100_144

**Symbol:** APE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 227 |
| net_profit_factor | 0.7743 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0478 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -1.1362 |
| sortino_ratio | -0.2465 |
| max_drawdown | 0.2594 |
| cagr | -0.1071 |
| net_avg_win | 72.6005 |
| net_avg_loss | -99.7286 |
| avg_hold_time_bars | 6.7621 |
| exposure | 0.0698 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
