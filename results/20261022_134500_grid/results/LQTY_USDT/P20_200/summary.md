# EMA Hourly Continuation — LQTY/USDT P20_200

**Symbol:** LQTY/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.7378 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9761 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.6522 |
| sortino_ratio | -0.4337 |
| max_drawdown | 0.4242 |
| cagr | -0.1827 |
| net_avg_win | 66.0466 |
| net_avg_loss | -87.4565 |
| avg_hold_time_bars | 43.6221 |
| exposure | 0.6790 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
