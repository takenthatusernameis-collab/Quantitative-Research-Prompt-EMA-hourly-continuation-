# EMA Hourly Continuation — ERG/USDT P34_200

**Symbol:** ERG/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.4963 |
| net_win_rate | 0.4249 |
| gross_profit_factor | 0.7290 |
| gross_win_rate | 0.4249 |
| sharpe_ratio | -4.6921 |
| sortino_ratio | -1.4266 |
| max_drawdown | 0.8318 |
| cagr | -0.5028 |
| net_avg_win | 40.5468 |
| net_avg_loss | -60.3705 |
| avg_hold_time_bars | 21.1543 |
| exposure | 0.4548 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
