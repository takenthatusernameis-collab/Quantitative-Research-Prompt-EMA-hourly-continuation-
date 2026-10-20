# EMA Hourly Continuation — DYDX/USDT P21_144

**Symbol:** DYDX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7030 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 1.0173 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -2.4986 |
| sortino_ratio | -0.7700 |
| max_drawdown | 0.6227 |
| cagr | -0.3061 |
| net_avg_win | 59.9870 |
| net_avg_loss | -83.5648 |
| avg_hold_time_bars | 26.0710 |
| exposure | 0.5676 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
