# EMA Hourly Continuation — GLM/USDT P55_89

**Symbol:** GLM/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 644 |
| net_profit_factor | 0.4233 |
| net_win_rate | 0.4332 |
| gross_profit_factor | 0.8406 |
| gross_win_rate | 0.4689 |
| sharpe_ratio | -6.2716 |
| sortino_ratio | -2.2660 |
| max_drawdown | 0.9354 |
| cagr | -0.6631 |
| net_avg_win | 24.5938 |
| net_avg_loss | -44.4136 |
| avg_hold_time_bars | 4.6988 |
| exposure | 0.1375 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
