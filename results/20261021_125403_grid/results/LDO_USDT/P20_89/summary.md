# EMA Hourly Continuation — LDO/USDT P20_89

**Symbol:** LDO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6928 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.8343 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -2.6434 |
| sortino_ratio | -0.8261 |
| max_drawdown | 0.6354 |
| cagr | -0.3165 |
| net_avg_win | 63.0760 |
| net_avg_loss | -75.3053 |
| avg_hold_time_bars | 16.3909 |
| exposure | 0.3621 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
