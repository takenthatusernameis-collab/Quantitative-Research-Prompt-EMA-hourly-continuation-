# EMA Hourly Continuation — FLR/USDT P12_100

**Symbol:** FLR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 883 |
| net_profit_factor | 0.5756 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9858 |
| gross_win_rate | 0.4904 |
| sharpe_ratio | -5.2987 |
| sortino_ratio | -2.2001 |
| max_drawdown | 0.9357 |
| cagr | -0.6586 |
| net_avg_win | 30.2587 |
| net_avg_loss | -47.2586 |
| avg_hold_time_bars | 12.7135 |
| exposure | 0.5103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
