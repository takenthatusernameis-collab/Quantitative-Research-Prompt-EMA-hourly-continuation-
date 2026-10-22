# EMA Hourly Continuation — TAIKO/USDT P20_89

**Symbol:** TAIKO/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 449 |
| net_profit_factor | 0.8390 |
| net_win_rate | 0.5234 |
| gross_profit_factor | 1.0814 |
| gross_win_rate | 0.5234 |
| sharpe_ratio | -1.1573 |
| sortino_ratio | -0.3629 |
| max_drawdown | 0.4237 |
| cagr | -0.1559 |
| net_avg_win | 73.5013 |
| net_avg_loss | -96.2029 |
| avg_hold_time_bars | 18.2717 |
| exposure | 0.3941 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
