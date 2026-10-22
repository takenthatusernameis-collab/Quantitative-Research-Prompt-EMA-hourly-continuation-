# EMA Hourly Continuation — BSV/USDT P26_100

**Symbol:** BSV/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.5020 |
| net_win_rate | 0.4326 |
| gross_profit_factor | 0.8249 |
| gross_win_rate | 0.4466 |
| sharpe_ratio | -6.0414 |
| sortino_ratio | -2.2536 |
| max_drawdown | 0.9397 |
| cagr | -0.6676 |
| net_avg_win | 30.6667 |
| net_avg_loss | -46.5745 |
| avg_hold_time_bars | 11.6994 |
| exposure | 0.3786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
