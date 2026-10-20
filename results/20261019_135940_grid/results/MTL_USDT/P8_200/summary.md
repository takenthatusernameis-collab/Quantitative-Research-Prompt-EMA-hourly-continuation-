# EMA Hourly Continuation — MTL/USDT P8_200

**Symbol:** MTL/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 256 |
| net_profit_factor | 0.8682 |
| net_win_rate | 0.5391 |
| gross_profit_factor | 1.1930 |
| gross_win_rate | 0.5469 |
| sharpe_ratio | -0.6355 |
| sortino_ratio | -0.1454 |
| max_drawdown | 0.1937 |
| cagr | -0.0676 |
| net_avg_win | 77.2304 |
| net_avg_loss | -104.0336 |
| avg_hold_time_bars | 73.6289 |
| exposure | 0.8530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
