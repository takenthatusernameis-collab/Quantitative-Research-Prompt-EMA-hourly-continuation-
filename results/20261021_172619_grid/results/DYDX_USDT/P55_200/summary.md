# EMA Hourly Continuation — DYDX/USDT P55_200

**Symbol:** DYDX/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 296 |
| net_profit_factor | 0.8875 |
| net_win_rate | 0.5203 |
| gross_profit_factor | 1.0731 |
| gross_win_rate | 0.5203 |
| sharpe_ratio | -0.5887 |
| sortino_ratio | -0.1457 |
| max_drawdown | 0.2335 |
| cagr | -0.0676 |
| net_avg_win | 82.5429 |
| net_avg_loss | -100.8654 |
| avg_hold_time_bars | 27.0946 |
| exposure | 0.3645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
