# EMA Hourly Continuation — NOT/USDT P55_144

**Symbol:** NOT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.6719 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9479 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -2.8592 |
| sortino_ratio | -0.9206 |
| max_drawdown | 0.6455 |
| cagr | -0.3474 |
| net_avg_win | 54.8421 |
| net_avg_loss | -77.7554 |
| avg_hold_time_bars | 10.5182 |
| exposure | 0.2441 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
