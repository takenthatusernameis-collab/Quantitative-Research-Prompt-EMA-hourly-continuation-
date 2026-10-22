# EMA Hourly Continuation — AVA/USDT P20_200

**Symbol:** AVA/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.8490 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0149 |
| gross_win_rate | 0.5086 |
| sharpe_ratio | -0.8335 |
| sortino_ratio | -0.2237 |
| max_drawdown | 0.3566 |
| cagr | -0.1002 |
| net_avg_win | 73.5674 |
| net_avg_loss | -89.6698 |
| avg_hold_time_bars | 35.1886 |
| exposure | 0.5598 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
