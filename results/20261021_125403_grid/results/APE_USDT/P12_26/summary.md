# EMA Hourly Continuation — APE/USDT P12_26

**Symbol:** APE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 443 |
| net_profit_factor | 0.6339 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4582 |
| sharpe_ratio | -3.1805 |
| sortino_ratio | -0.9551 |
| max_drawdown | 0.6808 |
| cagr | -0.3550 |
| net_avg_win | 56.9371 |
| net_avg_loss | -75.9731 |
| avg_hold_time_bars | 4.9684 |
| exposure | 0.1000 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
