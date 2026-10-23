# EMA Hourly Continuation — XAI/USDT P26_100

**Symbol:** XAI/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.6839 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.9834 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -4.3062 |
| sortino_ratio | -1.5402 |
| max_drawdown | 0.8722 |
| cagr | -0.5233 |
| net_avg_win | 61.7315 |
| net_avg_loss | -75.0474 |
| avg_hold_time_bars | 13.8359 |
| exposure | 0.4100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
