# EMA Hourly Continuation — METIS/USDT P26_89

**Symbol:** METIS/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 713 |
| net_profit_factor | 0.5568 |
| net_win_rate | 0.4488 |
| gross_profit_factor | 0.8647 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -5.2377 |
| sortino_ratio | -1.9682 |
| max_drawdown | 0.9111 |
| cagr | -0.6120 |
| net_avg_win | 35.6249 |
| net_avg_loss | -52.0928 |
| avg_hold_time_bars | 9.5302 |
| exposure | 0.3089 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
