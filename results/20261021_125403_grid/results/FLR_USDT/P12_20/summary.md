# EMA Hourly Continuation — FLR/USDT P12_20

**Symbol:** FLR/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 330 |
| net_profit_factor | 0.4599 |
| net_win_rate | 0.3939 |
| gross_profit_factor | 0.6665 |
| gross_win_rate | 0.3939 |
| sharpe_ratio | -4.6206 |
| sortino_ratio | -1.1993 |
| max_drawdown | 0.7597 |
| cagr | -0.4276 |
| net_avg_win | 49.3585 |
| net_avg_loss | -69.7674 |
| avg_hold_time_bars | 4.9848 |
| exposure | 0.0748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
