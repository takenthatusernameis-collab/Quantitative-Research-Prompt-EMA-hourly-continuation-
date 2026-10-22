# EMA Hourly Continuation — MOCA/USDT P12_50

**Symbol:** MOCA/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 612 |
| net_profit_factor | 0.7298 |
| net_win_rate | 0.4853 |
| gross_profit_factor | 0.9565 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -2.8295 |
| sortino_ratio | -1.0494 |
| max_drawdown | 0.6908 |
| cagr | -0.3823 |
| net_avg_win | 60.5876 |
| net_avg_loss | -78.2724 |
| avg_hold_time_bars | 9.8464 |
| exposure | 0.3021 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
