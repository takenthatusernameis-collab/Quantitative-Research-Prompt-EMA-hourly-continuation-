# EMA Hourly Continuation — MANTA/USDT P21_55

**Symbol:** MANTA/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 901 |
| net_profit_factor | 0.5466 |
| net_win_rate | 0.4528 |
| gross_profit_factor | 0.8767 |
| gross_win_rate | 0.4617 |
| sharpe_ratio | -6.0617 |
| sortino_ratio | -2.5750 |
| max_drawdown | 0.9547 |
| cagr | -0.7073 |
| net_avg_win | 28.1986 |
| net_avg_loss | -42.6932 |
| avg_hold_time_bars | 6.0477 |
| exposure | 0.2477 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
