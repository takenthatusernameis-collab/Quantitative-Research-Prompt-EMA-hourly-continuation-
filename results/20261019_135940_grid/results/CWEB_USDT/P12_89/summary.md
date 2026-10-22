# EMA Hourly Continuation — CWEB/USDT P12_89

**Symbol:** CWEB/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.5269 |
| net_win_rate | 0.4378 |
| gross_profit_factor | 0.8175 |
| gross_win_rate | 0.4414 |
| sharpe_ratio | -5.1783 |
| sortino_ratio | -1.7009 |
| max_drawdown | 0.8848 |
| cagr | -0.5743 |
| net_avg_win | 40.4675 |
| net_avg_loss | -59.8156 |
| avg_hold_time_bars | 23.8559 |
| exposure | 0.6018 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
