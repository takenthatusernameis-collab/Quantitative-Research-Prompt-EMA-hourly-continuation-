# EMA Hourly Continuation — PEOPLE/USDT P26_144

**Symbol:** PEOPLE/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.8754 |
| net_win_rate | 0.5123 |
| gross_profit_factor | 1.0411 |
| gross_win_rate | 0.5123 |
| sharpe_ratio | -0.6985 |
| sortino_ratio | -0.1806 |
| max_drawdown | 0.2733 |
| cagr | -0.0822 |
| net_avg_win | 81.8816 |
| net_avg_loss | -98.2418 |
| avg_hold_time_bars | 34.9540 |
| exposure | 0.5156 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
