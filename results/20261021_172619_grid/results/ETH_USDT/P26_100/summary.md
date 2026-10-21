# EMA Hourly Continuation — ETH/USDT P26_100

**Symbol:** ETH/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.6685 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9542 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -2.3590 |
| sortino_ratio | -0.6431 |
| max_drawdown | 0.5417 |
| cagr | -0.2553 |
| net_avg_win | 59.2688 |
| net_avg_loss | -85.2999 |
| avg_hold_time_bars | 20.4105 |
| exposure | 0.3368 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
