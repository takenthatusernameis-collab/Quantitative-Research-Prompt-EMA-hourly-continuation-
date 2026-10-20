# EMA Hourly Continuation — AVA/USDT P21_89

**Symbol:** AVA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 707 |
| net_profit_factor | 0.5245 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 0.8747 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -5.1362 |
| sortino_ratio | -1.9141 |
| max_drawdown | 0.9096 |
| cagr | -0.6104 |
| net_avg_win | 30.4724 |
| net_avg_loss | -50.2841 |
| avg_hold_time_bars | 11.0198 |
| exposure | 0.3541 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
