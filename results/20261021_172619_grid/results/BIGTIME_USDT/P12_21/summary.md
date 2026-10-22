# EMA Hourly Continuation — BIGTIME/USDT P12_21

**Symbol:** BIGTIME/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 438 |
| net_profit_factor | 0.5942 |
| net_win_rate | 0.4566 |
| gross_profit_factor | 0.8603 |
| gross_win_rate | 0.4589 |
| sharpe_ratio | -3.6475 |
| sortino_ratio | -1.0888 |
| max_drawdown | 0.7176 |
| cagr | -0.3941 |
| net_avg_win | 52.5317 |
| net_avg_loss | -74.2911 |
| avg_hold_time_bars | 5.5297 |
| exposure | 0.1096 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
