# EMA Hourly Continuation — APE/USDT P20_200

**Symbol:** APE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 308 |
| net_profit_factor | 0.7681 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.9054 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -1.3418 |
| sortino_ratio | -0.3355 |
| max_drawdown | 0.3342 |
| cagr | -0.1442 |
| net_avg_win | 72.4582 |
| net_avg_loss | -87.2549 |
| avg_hold_time_bars | 42.6883 |
| exposure | 0.5976 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
