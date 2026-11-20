# EMA Hourly Continuation — P2P/USDT P50_144

**Symbol:** P2P/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.5130 |
| net_win_rate | 0.4040 |
| gross_profit_factor | 0.6911 |
| gross_win_rate | 0.4062 |
| sharpe_ratio | -4.2690 |
| sortino_ratio | -1.2703 |
| max_drawdown | 0.7832 |
| cagr | -0.4560 |
| net_avg_win | 45.0795 |
| net_avg_loss | -59.5620 |
| avg_hold_time_bars | 11.7815 |
| exposure | 0.2426 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
