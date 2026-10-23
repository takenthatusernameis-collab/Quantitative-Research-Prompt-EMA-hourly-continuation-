# EMA Hourly Continuation — ALEX/USDT P20_89

**Symbol:** ALEX/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.6033 |
| net_win_rate | 0.4375 |
| gross_profit_factor | 0.8823 |
| gross_win_rate | 0.4429 |
| sharpe_ratio | -4.5093 |
| sortino_ratio | -1.4995 |
| max_drawdown | 0.8476 |
| cagr | -0.5119 |
| net_avg_win | 51.8196 |
| net_avg_loss | -66.8088 |
| avg_hold_time_bars | 18.5000 |
| exposure | 0.4709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
