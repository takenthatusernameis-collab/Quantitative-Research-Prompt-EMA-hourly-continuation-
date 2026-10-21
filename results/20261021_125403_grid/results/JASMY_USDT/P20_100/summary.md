# EMA Hourly Continuation — JASMY/USDT P20_100

**Symbol:** JASMY/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.9965 |
| net_win_rate | 0.5504 |
| gross_profit_factor | 1.2125 |
| gross_win_rate | 0.5504 |
| sharpe_ratio | 0.0456 |
| sortino_ratio | 0.0141 |
| max_drawdown | 0.2129 |
| cagr | -0.0029 |
| net_avg_win | 81.5196 |
| net_avg_loss | -100.1657 |
| avg_hold_time_bars | 18.9627 |
| exposure | 0.3930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
