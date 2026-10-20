# EMA Hourly Continuation — WIN/USDT P100_144

**Symbol:** WIN/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 477 |
| net_profit_factor | 0.2094 |
| net_win_rate | 0.3648 |
| gross_profit_factor | 0.5719 |
| gross_win_rate | 0.3899 |
| sharpe_ratio | -8.4185 |
| sortino_ratio | -2.6775 |
| max_drawdown | 0.9683 |
| cagr | -0.7470 |
| net_avg_win | 14.7437 |
| net_avg_loss | -40.4236 |
| avg_hold_time_bars | 3.9497 |
| exposure | 0.0856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
