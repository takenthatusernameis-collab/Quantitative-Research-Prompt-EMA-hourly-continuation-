# EMA Hourly Continuation — AUCTION/USDT P89_100

**Symbol:** AUCTION/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 226 |
| net_profit_factor | 0.4932 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8709 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -3.4003 |
| sortino_ratio | -0.7194 |
| max_drawdown | 0.5939 |
| cagr | -0.2959 |
| net_avg_win | 55.4759 |
| net_avg_loss | -94.1936 |
| avg_hold_time_bars | 5.5310 |
| exposure | 0.0566 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
