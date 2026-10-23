# EMA Hourly Continuation — LPT/USDT P21_144

**Symbol:** LPT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.6247 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8708 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -3.4933 |
| sortino_ratio | -1.1388 |
| max_drawdown | 0.7516 |
| cagr | -0.4189 |
| net_avg_win | 49.1612 |
| net_avg_loss | -68.6173 |
| avg_hold_time_bars | 20.4566 |
| exposure | 0.5030 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
