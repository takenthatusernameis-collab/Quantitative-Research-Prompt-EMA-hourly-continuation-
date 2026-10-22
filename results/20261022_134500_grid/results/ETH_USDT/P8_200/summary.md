# EMA Hourly Continuation — ETH/USDT P8_200

**Symbol:** ETH/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.4657 |
| net_win_rate | 0.4599 |
| gross_profit_factor | 0.8722 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -3.5000 |
| sortino_ratio | -0.8287 |
| max_drawdown | 0.6549 |
| cagr | -0.3340 |
| net_avg_win | 42.2361 |
| net_avg_loss | -77.2366 |
| avg_hold_time_bars | 63.9930 |
| exposure | 0.8348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
