# EMA Hourly Continuation — CELO/USDT P20_34

**Symbol:** CELO/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1120 |
| net_profit_factor | 0.3455 |
| net_win_rate | 0.4330 |
| gross_profit_factor | 0.7278 |
| gross_win_rate | 0.4554 |
| sharpe_ratio | -9.7434 |
| sortino_ratio | -4.5942 |
| max_drawdown | 0.9972 |
| cagr | -0.9027 |
| net_avg_win | 10.8533 |
| net_avg_loss | -23.9934 |
| avg_hold_time_bars | 2.9920 |
| exposure | 0.1516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
