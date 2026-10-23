# EMA Hourly Continuation — ANYONE/USDT P12_89

**Symbol:** ANYONE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 676 |
| net_profit_factor | 0.6730 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.8503 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -3.6613 |
| sortino_ratio | -1.4159 |
| max_drawdown | 0.7896 |
| cagr | -0.4866 |
| net_avg_win | 52.3414 |
| net_avg_loss | -64.3213 |
| avg_hold_time_bars | 14.7707 |
| exposure | 0.5045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
