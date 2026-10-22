# EMA Hourly Continuation — GRT/USDT P8_144

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.6967 |
| net_win_rate | 0.4969 |
| gross_profit_factor | 1.0025 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -2.5647 |
| sortino_ratio | -0.7852 |
| max_drawdown | 0.6439 |
| cagr | -0.3164 |
| net_avg_win | 59.5532 |
| net_avg_loss | -84.4099 |
| avg_hold_time_bars | 34.6764 |
| exposure | 0.7516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
