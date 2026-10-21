# EMA Hourly Continuation — OSMO/USDT P12_34

**Symbol:** OSMO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 682 |
| net_profit_factor | 0.6713 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.9753 |
| gross_win_rate | 0.4457 |
| sharpe_ratio | -4.7473 |
| sortino_ratio | -1.7700 |
| max_drawdown | 0.8860 |
| cagr | -0.5561 |
| net_avg_win | 58.4461 |
| net_avg_loss | -70.0177 |
| avg_hold_time_bars | 6.5601 |
| exposure | 0.2034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
