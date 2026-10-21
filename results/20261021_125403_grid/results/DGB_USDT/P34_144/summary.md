# EMA Hourly Continuation — DGB/USDT P34_144

**Symbol:** DGB/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 397 |
| net_profit_factor | 0.7080 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8759 |
| gross_win_rate | 0.4635 |
| sharpe_ratio | -2.2671 |
| sortino_ratio | -0.6421 |
| max_drawdown | 0.5296 |
| cagr | -0.2562 |
| net_avg_win | 69.1225 |
| net_avg_loss | -84.3326 |
| avg_hold_time_bars | 21.0252 |
| exposure | 0.3794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
