# EMA Hourly Continuation — LDO/USDT P8_21

**Symbol:** LDO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.6926 |
| net_win_rate | 0.4863 |
| gross_profit_factor | 0.9151 |
| gross_win_rate | 0.4863 |
| sharpe_ratio | -2.5631 |
| sortino_ratio | -0.8849 |
| max_drawdown | 0.6556 |
| cagr | -0.3332 |
| net_avg_win | 50.8420 |
| net_avg_loss | -69.4795 |
| avg_hold_time_bars | 4.8299 |
| exposure | 0.1278 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
