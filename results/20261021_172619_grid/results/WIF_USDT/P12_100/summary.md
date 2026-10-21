# EMA Hourly Continuation — WIF/USDT P12_100

**Symbol:** WIF/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.8469 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9814 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -1.1910 |
| sortino_ratio | -0.3622 |
| max_drawdown | 0.4498 |
| cagr | -0.1562 |
| net_avg_win | 85.7541 |
| net_avg_loss | -99.0453 |
| avg_hold_time_bars | 25.5916 |
| exposure | 0.5270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
