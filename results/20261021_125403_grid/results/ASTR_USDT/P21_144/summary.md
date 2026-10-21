# EMA Hourly Continuation — ASTR/USDT P21_144

**Symbol:** ASTR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.7987 |
| net_win_rate | 0.5027 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.5027 |
| sharpe_ratio | -1.4101 |
| sortino_ratio | -0.3883 |
| max_drawdown | 0.4362 |
| cagr | -0.1645 |
| net_avg_win | 77.3119 |
| net_avg_loss | -97.8467 |
| avg_hold_time_bars | 34.1478 |
| exposure | 0.5748 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
