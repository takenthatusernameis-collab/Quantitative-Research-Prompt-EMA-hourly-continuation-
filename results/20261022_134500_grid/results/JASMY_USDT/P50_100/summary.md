# EMA Hourly Continuation — JASMY/USDT P50_100

**Symbol:** JASMY/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 632 |
| net_profit_factor | 0.5580 |
| net_win_rate | 0.4778 |
| gross_profit_factor | 0.8879 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -4.4237 |
| sortino_ratio | -1.5660 |
| max_drawdown | 0.8529 |
| cagr | -0.5289 |
| net_avg_win | 35.4847 |
| net_avg_loss | -58.2010 |
| avg_hold_time_bars | 6.0206 |
| exposure | 0.1730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
