# EMA Hourly Continuation — ARKM/USDT P20_89

**Symbol:** ARKM/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.7531 |
| net_win_rate | 0.4760 |
| gross_profit_factor | 0.9125 |
| gross_win_rate | 0.4760 |
| sharpe_ratio | -2.0624 |
| sortino_ratio | -0.6569 |
| max_drawdown | 0.5515 |
| cagr | -0.2614 |
| net_avg_win | 68.2786 |
| net_avg_loss | -82.3578 |
| avg_hold_time_bars | 15.5860 |
| exposure | 0.3542 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
