# EMA Hourly Continuation — TAO/USDT P89_144

**Symbol:** TAO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 210 |
| net_profit_factor | 0.6771 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8489 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -1.7731 |
| sortino_ratio | -0.3651 |
| max_drawdown | 0.3432 |
| cagr | -0.1541 |
| net_avg_win | 74.9547 |
| net_avg_loss | -93.2238 |
| avg_hold_time_bars | 7.5095 |
| exposure | 0.0717 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
