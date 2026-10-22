# EMA Hourly Continuation — APT/USDT P20_50

**Symbol:** APT/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1025 |
| net_profit_factor | 0.4493 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.8386 |
| gross_win_rate | 0.4654 |
| sharpe_ratio | -7.4017 |
| sortino_ratio | -3.3468 |
| max_drawdown | 0.9851 |
| cagr | -0.8060 |
| net_avg_win | 17.2948 |
| net_avg_loss | -31.8396 |
| avg_hold_time_bars | 4.5590 |
| exposure | 0.2124 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
