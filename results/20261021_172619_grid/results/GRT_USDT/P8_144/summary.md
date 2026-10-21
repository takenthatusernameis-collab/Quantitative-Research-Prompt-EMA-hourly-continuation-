# EMA Hourly Continuation — GRT/USDT P8_144

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 357 |
| net_profit_factor | 0.8774 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0481 |
| gross_win_rate | 0.5154 |
| sharpe_ratio | -0.7469 |
| sortino_ratio | -0.2019 |
| max_drawdown | 0.3606 |
| cagr | -0.0917 |
| net_avg_win | 83.8034 |
| net_avg_loss | -101.5907 |
| avg_hold_time_bars | 45.8936 |
| exposure | 0.7414 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
