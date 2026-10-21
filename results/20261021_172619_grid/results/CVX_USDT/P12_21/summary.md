# EMA Hourly Continuation — CVX/USDT P12_21

**Symbol:** CVX/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.6995 |
| net_win_rate | 0.5025 |
| gross_profit_factor | 0.9934 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -2.1495 |
| sortino_ratio | -0.6210 |
| max_drawdown | 0.5365 |
| cagr | -0.2466 |
| net_avg_win | 58.3521 |
| net_avg_loss | -84.2500 |
| avg_hold_time_bars | 4.7723 |
| exposure | 0.0876 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
