# EMA Hourly Continuation — YGG/USDT P55_144

**Symbol:** YGG/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.8869 |
| net_win_rate | 0.5265 |
| gross_profit_factor | 1.1025 |
| gross_win_rate | 0.5265 |
| sharpe_ratio | -0.7109 |
| sortino_ratio | -0.1988 |
| max_drawdown | 0.2982 |
| cagr | -0.0903 |
| net_avg_win | 83.6389 |
| net_avg_loss | -104.8469 |
| avg_hold_time_bars | 14.2804 |
| exposure | 0.2443 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
