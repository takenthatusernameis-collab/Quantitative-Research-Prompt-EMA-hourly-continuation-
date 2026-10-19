# EMA Hourly Continuation — LDO/USDT P34_55

**Symbol:** LDO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 941 |
| net_profit_factor | 0.4009 |
| net_win_rate | 0.4283 |
| gross_profit_factor | 0.7204 |
| gross_win_rate | 0.4378 |
| sharpe_ratio | -8.2435 |
| sortino_ratio | -3.5930 |
| max_drawdown | 0.9880 |
| cagr | -0.8272 |
| net_avg_win | 16.4042 |
| net_avg_loss | -30.6490 |
| avg_hold_time_bars | 3.0414 |
| exposure | 0.1301 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
