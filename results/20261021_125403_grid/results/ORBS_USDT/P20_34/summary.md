# EMA Hourly Continuation — ORBS/USDT P20_34

**Symbol:** ORBS/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.4773 |
| net_win_rate | 0.4017 |
| gross_profit_factor | 0.7780 |
| gross_win_rate | 0.4037 |
| sharpe_ratio | -5.9211 |
| sortino_ratio | -1.8653 |
| max_drawdown | 0.8916 |
| cagr | -0.5793 |
| net_avg_win | 41.7112 |
| net_avg_loss | -58.6681 |
| avg_hold_time_bars | 6.3789 |
| exposure | 0.1400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
