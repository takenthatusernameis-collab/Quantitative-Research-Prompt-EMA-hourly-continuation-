# EMA Hourly Continuation — MTL/USDT P12_89

**Symbol:** MTL/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 542 |
| net_profit_factor | 0.6303 |
| net_win_rate | 0.4686 |
| gross_profit_factor | 0.9569 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -3.8915 |
| sortino_ratio | -1.2728 |
| max_drawdown | 0.7909 |
| cagr | -0.4567 |
| net_avg_win | 52.7247 |
| net_avg_loss | -73.7696 |
| avg_hold_time_bars | 26.0443 |
| exposure | 0.6388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
