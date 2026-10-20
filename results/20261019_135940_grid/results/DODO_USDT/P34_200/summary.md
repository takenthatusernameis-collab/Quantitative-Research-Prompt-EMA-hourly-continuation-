# EMA Hourly Continuation — DODO/USDT P34_200

**Symbol:** DODO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.5758 |
| net_win_rate | 0.4476 |
| gross_profit_factor | 0.7931 |
| gross_win_rate | 0.4517 |
| sharpe_ratio | -3.6142 |
| sortino_ratio | -1.1216 |
| max_drawdown | 0.7530 |
| cagr | -0.4111 |
| net_avg_win | 45.9020 |
| net_avg_loss | -64.5999 |
| avg_hold_time_bars | 20.8172 |
| exposure | 0.4588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
