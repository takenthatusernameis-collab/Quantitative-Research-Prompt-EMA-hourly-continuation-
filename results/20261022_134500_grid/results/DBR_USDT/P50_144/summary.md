# EMA Hourly Continuation — DBR/USDT P50_144

**Symbol:** DBR/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 341 |
| net_profit_factor | 0.5151 |
| net_win_rate | 0.4457 |
| gross_profit_factor | 0.8661 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -4.2387 |
| sortino_ratio | -1.2322 |
| max_drawdown | 0.7058 |
| cagr | -0.4468 |
| net_avg_win | 48.6000 |
| net_avg_loss | -75.8753 |
| avg_hold_time_bars | 15.4018 |
| exposure | 0.2987 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
