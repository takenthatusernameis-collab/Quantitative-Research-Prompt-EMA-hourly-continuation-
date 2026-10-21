# EMA Hourly Continuation — ENJ/USDT P12_144

**Symbol:** ENJ/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 327 |
| net_profit_factor | 0.8470 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0154 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -0.9181 |
| sortino_ratio | -0.2371 |
| max_drawdown | 0.3411 |
| cagr | -0.1056 |
| net_avg_win | 82.3129 |
| net_avg_loss | -98.9872 |
| avg_hold_time_bars | 47.4373 |
| exposure | 0.7019 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
