# EMA Hourly Continuation — LUNC/USDT P20_144

**Symbol:** LUNC/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 604 |
| net_profit_factor | 0.6018 |
| net_win_rate | 0.4868 |
| gross_profit_factor | 0.9363 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -3.7899 |
| sortino_ratio | -1.3088 |
| max_drawdown | 0.8046 |
| cagr | -0.4678 |
| net_avg_win | 40.8517 |
| net_avg_loss | -64.3818 |
| avg_hold_time_bars | 17.9470 |
| exposure | 0.4927 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
