# EMA Hourly Continuation — TAO/USDT P12_26

**Symbol:** TAO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7529 |
| net_win_rate | 0.4866 |
| gross_profit_factor | 0.9616 |
| gross_win_rate | 0.4866 |
| sharpe_ratio | -1.8456 |
| sortino_ratio | -0.5104 |
| max_drawdown | 0.5013 |
| cagr | -0.2097 |
| net_avg_win | 74.6857 |
| net_avg_loss | -94.0366 |
| avg_hold_time_bars | 5.4385 |
| exposure | 0.0925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
