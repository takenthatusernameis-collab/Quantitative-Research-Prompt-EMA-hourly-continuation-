# EMA Hourly Continuation — SUSHI/USDT P20_21

**Symbol:** SUSHI/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1267 |
| net_profit_factor | 0.1261 |
| net_win_rate | 0.3031 |
| gross_profit_factor | 0.6354 |
| gross_win_rate | 0.3686 |
| sharpe_ratio | -18.2348 |
| sortino_ratio | -9.8555 |
| max_drawdown | 1.0000 |
| cagr | -0.9961 |
| net_avg_win | 3.7562 |
| net_avg_loss | -12.9585 |
| avg_hold_time_bars | 1.6077 |
| exposure | 0.0922 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
