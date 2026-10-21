# EMA Hourly Continuation — BAT/USDT P26_144

**Symbol:** BAT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 422 |
| net_profit_factor | 0.8291 |
| net_win_rate | 0.5190 |
| gross_profit_factor | 1.0663 |
| gross_win_rate | 0.5190 |
| sharpe_ratio | -1.1520 |
| sortino_ratio | -0.3399 |
| max_drawdown | 0.3825 |
| cagr | -0.1464 |
| net_avg_win | 72.6595 |
| net_avg_loss | -94.5466 |
| avg_hold_time_bars | 23.6706 |
| exposure | 0.4540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
