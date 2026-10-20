# EMA Hourly Continuation — OGN/USDT P20_26

**Symbol:** OGN/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1155 |
| net_profit_factor | 0.2647 |
| net_win_rate | 0.3619 |
| gross_profit_factor | 0.7606 |
| gross_win_rate | 0.4268 |
| sharpe_ratio | -13.9507 |
| sortino_ratio | -6.8486 |
| max_drawdown | 0.9999 |
| cagr | -0.9741 |
| net_avg_win | 8.6125 |
| net_avg_loss | -18.4519 |
| avg_hold_time_bars | 2.5818 |
| exposure | 0.1349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
