# EMA Hourly Continuation — REQ/USDT P20_200

**Symbol:** REQ/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.4695 |
| net_win_rate | 0.3951 |
| gross_profit_factor | 0.8236 |
| gross_win_rate | 0.4213 |
| sharpe_ratio | -7.2071 |
| sortino_ratio | -2.5917 |
| max_drawdown | 0.9591 |
| cagr | -0.7201 |
| net_avg_win | 33.1528 |
| net_avg_loss | -46.1184 |
| avg_hold_time_bars | 18.8318 |
| exposure | 0.5547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
