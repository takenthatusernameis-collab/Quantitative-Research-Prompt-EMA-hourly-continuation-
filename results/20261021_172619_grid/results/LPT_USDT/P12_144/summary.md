# EMA Hourly Continuation — LPT/USDT P12_144

**Symbol:** LPT/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.7679 |
| net_win_rate | 0.4731 |
| gross_profit_factor | 0.9130 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -1.7803 |
| sortino_ratio | -0.5005 |
| max_drawdown | 0.4980 |
| cagr | -0.2063 |
| net_avg_win | 78.7162 |
| net_avg_loss | -92.0637 |
| avg_hold_time_bars | 37.2813 |
| exposure | 0.6626 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
