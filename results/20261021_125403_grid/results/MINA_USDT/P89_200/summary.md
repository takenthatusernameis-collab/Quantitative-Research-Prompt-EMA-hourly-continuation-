# EMA Hourly Continuation — MINA/USDT P89_200

**Symbol:** MINA/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 281 |
| net_profit_factor | 0.8517 |
| net_win_rate | 0.5302 |
| gross_profit_factor | 1.1031 |
| gross_win_rate | 0.5302 |
| sharpe_ratio | -0.7437 |
| sortino_ratio | -0.1797 |
| max_drawdown | 0.2623 |
| cagr | -0.0814 |
| net_avg_win | 74.0640 |
| net_avg_loss | -98.1549 |
| avg_hold_time_bars | 17.6085 |
| exposure | 0.2249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
