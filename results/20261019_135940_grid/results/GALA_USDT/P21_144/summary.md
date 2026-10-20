# EMA Hourly Continuation — GALA/USDT P21_144

**Symbol:** GALA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6306 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.8866 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -3.0500 |
| sortino_ratio | -0.8993 |
| max_drawdown | 0.6605 |
| cagr | -0.3471 |
| net_avg_win | 55.2603 |
| net_avg_loss | -75.3836 |
| avg_hold_time_bars | 28.2073 |
| exposure | 0.5629 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
