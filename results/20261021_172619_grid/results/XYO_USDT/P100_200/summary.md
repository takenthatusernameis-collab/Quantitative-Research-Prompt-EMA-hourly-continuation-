# EMA Hourly Continuation — XYO/USDT P100_200

**Symbol:** XYO/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.6069 |
| net_win_rate | 0.4494 |
| gross_profit_factor | 0.8338 |
| gross_win_rate | 0.4494 |
| sharpe_ratio | -2.9883 |
| sortino_ratio | -0.7783 |
| max_drawdown | 0.6008 |
| cagr | -0.3011 |
| net_avg_win | 60.8364 |
| net_avg_loss | -81.8128 |
| avg_hold_time_bars | 11.6726 |
| exposure | 0.1775 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
