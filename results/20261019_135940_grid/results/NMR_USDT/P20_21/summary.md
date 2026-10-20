# EMA Hourly Continuation — NMR/USDT P20_21

**Symbol:** NMR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1291 |
| net_profit_factor | 0.1611 |
| net_win_rate | 0.2959 |
| gross_profit_factor | 0.6010 |
| gross_win_rate | 0.3927 |
| sharpe_ratio | -18.2455 |
| sortino_ratio | -9.9336 |
| max_drawdown | 1.0000 |
| cagr | -0.9961 |
| net_avg_win | 5.0289 |
| net_avg_loss | -13.1145 |
| avg_hold_time_bars | 1.9969 |
| exposure | 0.1172 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
