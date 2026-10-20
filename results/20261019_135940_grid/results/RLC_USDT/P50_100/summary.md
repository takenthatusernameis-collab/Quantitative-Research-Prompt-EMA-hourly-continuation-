# EMA Hourly Continuation — RLC/USDT P50_100

**Symbol:** RLC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 653 |
| net_profit_factor | 0.5337 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.8983 |
| gross_win_rate | 0.4809 |
| sharpe_ratio | -4.8431 |
| sortino_ratio | -1.7589 |
| max_drawdown | 0.8874 |
| cagr | -0.5673 |
| net_avg_win | 32.9458 |
| net_avg_loss | -54.1053 |
| avg_hold_time_bars | 6.1011 |
| exposure | 0.1811 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
