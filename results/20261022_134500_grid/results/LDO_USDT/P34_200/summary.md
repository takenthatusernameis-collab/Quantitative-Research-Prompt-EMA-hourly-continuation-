# EMA Hourly Continuation — LDO/USDT P34_200

**Symbol:** LDO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 385 |
| net_profit_factor | 0.5579 |
| net_win_rate | 0.4338 |
| gross_profit_factor | 0.7576 |
| gross_win_rate | 0.4442 |
| sharpe_ratio | -3.3592 |
| sortino_ratio | -0.9232 |
| max_drawdown | 0.6741 |
| cagr | -0.3551 |
| net_avg_win | 50.4603 |
| net_avg_loss | -69.2813 |
| avg_hold_time_bars | 28.7636 |
| exposure | 0.5034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
