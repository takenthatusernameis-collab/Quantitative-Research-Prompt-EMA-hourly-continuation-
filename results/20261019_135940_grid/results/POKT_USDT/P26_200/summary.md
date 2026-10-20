# EMA Hourly Continuation — POKT/USDT P26_200

**Symbol:** POKT/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 474 |
| net_profit_factor | 0.6697 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.9301 |
| gross_win_rate | 0.4705 |
| sharpe_ratio | -3.0723 |
| sortino_ratio | -0.9363 |
| max_drawdown | 0.6821 |
| cagr | -0.3604 |
| net_avg_win | 62.3058 |
| net_avg_loss | -80.5814 |
| avg_hold_time_bars | 27.3586 |
| exposure | 0.5868 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
