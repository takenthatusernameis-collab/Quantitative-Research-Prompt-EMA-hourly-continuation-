# EMA Hourly Continuation — LDO/USDT P21_100

**Symbol:** LDO/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 657 |
| net_profit_factor | 0.5761 |
| net_win_rate | 0.4414 |
| gross_profit_factor | 0.8190 |
| gross_win_rate | 0.4460 |
| sharpe_ratio | -4.7466 |
| sortino_ratio | -1.7047 |
| max_drawdown | 0.8744 |
| cagr | -0.5580 |
| net_avg_win | 40.8289 |
| net_avg_loss | -56.0044 |
| avg_hold_time_bars | 13.6834 |
| exposure | 0.4086 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
