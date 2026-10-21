# EMA Hourly Continuation — GTC/USDT P34_200

**Symbol:** GTC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 323 |
| net_profit_factor | 0.6309 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.7582 |
| gross_win_rate | 0.4365 |
| sharpe_ratio | -2.5148 |
| sortino_ratio | -0.6377 |
| max_drawdown | 0.5503 |
| cagr | -0.2545 |
| net_avg_win | 63.2446 |
| net_avg_loss | -77.6642 |
| avg_hold_time_bars | 32.2043 |
| exposure | 0.4728 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
