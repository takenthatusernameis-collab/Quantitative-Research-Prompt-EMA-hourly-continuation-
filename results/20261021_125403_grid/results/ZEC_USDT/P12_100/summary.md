# EMA Hourly Continuation — ZEC/USDT P12_100

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 440 |
| net_profit_factor | 0.9623 |
| net_win_rate | 0.5318 |
| gross_profit_factor | 1.1243 |
| gross_win_rate | 0.5318 |
| sharpe_ratio | -0.1812 |
| sortino_ratio | -0.0549 |
| max_drawdown | 0.2345 |
| cagr | -0.0322 |
| net_avg_win | 86.1507 |
| net_avg_loss | -101.6921 |
| avg_hold_time_bars | 27.7182 |
| exposure | 0.5544 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
