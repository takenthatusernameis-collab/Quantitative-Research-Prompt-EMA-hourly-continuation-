# EMA Hourly Continuation — LDO/USDT P20_50

**Symbol:** LDO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1039 |
| net_profit_factor | 0.4568 |
| net_win_rate | 0.4447 |
| gross_profit_factor | 0.8170 |
| gross_win_rate | 0.4572 |
| sharpe_ratio | -7.6274 |
| sortino_ratio | -3.4385 |
| max_drawdown | 0.9866 |
| cagr | -0.8195 |
| net_avg_win | 17.9528 |
| net_avg_loss | -31.4705 |
| avg_hold_time_bars | 4.3426 |
| exposure | 0.2051 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
