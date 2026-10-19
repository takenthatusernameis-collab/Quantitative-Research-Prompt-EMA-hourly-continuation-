# EMA Hourly Continuation — ICP/USDT P89_144

**Symbol:** ICP/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.4405 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.8484 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -5.3367 |
| sortino_ratio | -1.7362 |
| max_drawdown | 0.8822 |
| cagr | -0.5717 |
| net_avg_win | 28.5488 |
| net_avg_loss | -55.6487 |
| avg_hold_time_bars | 4.3992 |
| exposure | 0.1052 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
