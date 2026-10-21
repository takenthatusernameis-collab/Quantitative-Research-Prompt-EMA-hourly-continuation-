# EMA Hourly Continuation — LDO/USDT P20_144

**Symbol:** LDO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.7996 |
| net_win_rate | 0.4886 |
| gross_profit_factor | 0.9399 |
| gross_win_rate | 0.4886 |
| sharpe_ratio | -1.2696 |
| sortino_ratio | -0.3394 |
| max_drawdown | 0.3652 |
| cagr | -0.1460 |
| net_avg_win | 75.9049 |
| net_avg_loss | -90.7150 |
| avg_hold_time_bars | 34.4659 |
| exposure | 0.5515 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
