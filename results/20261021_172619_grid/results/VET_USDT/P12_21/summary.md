# EMA Hourly Continuation — VET/USDT P12_21

**Symbol:** VET/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.6288 |
| net_win_rate | 0.4858 |
| gross_profit_factor | 0.9252 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -2.4817 |
| sortino_ratio | -0.6344 |
| max_drawdown | 0.5413 |
| cagr | -0.2519 |
| net_avg_win | 56.9234 |
| net_avg_loss | -85.5304 |
| avg_hold_time_bars | 4.6215 |
| exposure | 0.0666 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
