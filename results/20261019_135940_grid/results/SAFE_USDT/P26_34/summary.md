# EMA Hourly Continuation — SAFE/USDT P26_34

**Symbol:** SAFE/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.3103 |
| net_win_rate | 0.4155 |
| gross_profit_factor | 0.8968 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -10.9329 |
| sortino_ratio | -5.0687 |
| max_drawdown | 0.9985 |
| cagr | -0.9257 |
| net_avg_win | 10.3280 |
| net_avg_loss | -23.6558 |
| avg_hold_time_bars | 2.7775 |
| exposure | 0.1332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
