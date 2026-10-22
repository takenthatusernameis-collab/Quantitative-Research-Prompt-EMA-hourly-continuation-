# EMA Hourly Continuation — NEO/USDT P144_200

**Symbol:** NEO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.3723 |
| net_win_rate | 0.4264 |
| gross_profit_factor | 0.8016 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -6.0761 |
| sortino_ratio | -1.8487 |
| max_drawdown | 0.8998 |
| cagr | -0.5986 |
| net_avg_win | 27.4849 |
| net_avg_loss | -54.8732 |
| avg_hold_time_bars | 4.0286 |
| exposure | 0.0833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
