# EMA Hourly Continuation — BIGTIME/USDT P20_89

**Symbol:** BIGTIME/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.8387 |
| net_win_rate | 0.5141 |
| gross_profit_factor | 1.0457 |
| gross_win_rate | 0.5141 |
| sharpe_ratio | -1.1880 |
| sortino_ratio | -0.3799 |
| max_drawdown | 0.4155 |
| cagr | -0.1624 |
| net_avg_win | 73.1962 |
| net_avg_loss | -92.3233 |
| avg_hold_time_bars | 18.3956 |
| exposure | 0.4146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
