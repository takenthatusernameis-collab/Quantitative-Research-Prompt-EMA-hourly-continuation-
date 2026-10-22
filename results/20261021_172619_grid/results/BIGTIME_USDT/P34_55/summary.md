# EMA Hourly Continuation — BIGTIME/USDT P34_55

**Symbol:** BIGTIME/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 393 |
| net_profit_factor | 0.7513 |
| net_win_rate | 0.5191 |
| gross_profit_factor | 1.0594 |
| gross_win_rate | 0.5191 |
| sharpe_ratio | -1.7451 |
| sortino_ratio | -0.4975 |
| max_drawdown | 0.4786 |
| cagr | -0.2033 |
| net_avg_win | 64.6263 |
| net_avg_loss | -92.8409 |
| avg_hold_time_bars | 6.0941 |
| exposure | 0.1084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
