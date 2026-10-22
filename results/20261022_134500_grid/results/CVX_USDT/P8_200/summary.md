# EMA Hourly Continuation — CVX/USDT P8_200

**Symbol:** CVX/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.8391 |
| net_win_rate | 0.5060 |
| gross_profit_factor | 1.0386 |
| gross_win_rate | 0.5100 |
| sharpe_ratio | -0.8247 |
| sortino_ratio | -0.1853 |
| max_drawdown | 0.2562 |
| cagr | -0.0841 |
| net_avg_win | 81.9009 |
| net_avg_loss | -99.9883 |
| avg_hold_time_bars | 75.7510 |
| exposure | 0.8574 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
