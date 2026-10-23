# EMA Hourly Continuation — DUSK/USDT P26_55

**Symbol:** DUSK/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 886 |
| net_profit_factor | 0.5142 |
| net_win_rate | 0.4424 |
| gross_profit_factor | 0.8830 |
| gross_win_rate | 0.4537 |
| sharpe_ratio | -6.4760 |
| sortino_ratio | -2.6985 |
| max_drawdown | 0.9645 |
| cagr | -0.7321 |
| net_avg_win | 26.0181 |
| net_avg_loss | -40.1481 |
| avg_hold_time_bars | 4.5248 |
| exposure | 0.1822 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
