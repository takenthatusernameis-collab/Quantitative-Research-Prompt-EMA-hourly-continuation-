# EMA Hourly Continuation — ZEC/USDT P12_200

**Symbol:** ZEC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.8381 |
| net_win_rate | 0.5248 |
| gross_profit_factor | 1.0885 |
| gross_win_rate | 0.5280 |
| sharpe_ratio | -0.8642 |
| sortino_ratio | -0.2208 |
| max_drawdown | 0.2808 |
| cagr | -0.1001 |
| net_avg_win | 71.2632 |
| net_avg_loss | -93.9239 |
| avg_hold_time_bars | 51.8913 |
| exposure | 0.7595 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
