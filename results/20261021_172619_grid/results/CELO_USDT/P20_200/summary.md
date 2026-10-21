# EMA Hourly Continuation — CELO/USDT P20_200

**Symbol:** CELO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 304 |
| net_profit_factor | 0.8619 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0255 |
| gross_win_rate | 0.5033 |
| sharpe_ratio | -0.8658 |
| sortino_ratio | -0.2156 |
| max_drawdown | 0.3459 |
| cagr | -0.0967 |
| net_avg_win | 92.2443 |
| net_avg_loss | -108.4454 |
| avg_hold_time_bars | 46.9572 |
| exposure | 0.6460 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
