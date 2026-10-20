# EMA Hourly Continuation — LPT/USDT P26_50

**Symbol:** LPT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1014 |
| net_profit_factor | 0.3976 |
| net_win_rate | 0.4043 |
| gross_profit_factor | 0.7015 |
| gross_win_rate | 0.4359 |
| sharpe_ratio | -9.2606 |
| sortino_ratio | -4.1787 |
| max_drawdown | 0.9946 |
| cagr | -0.8715 |
| net_avg_win | 16.0043 |
| net_avg_loss | -27.3244 |
| avg_hold_time_bars | 3.8067 |
| exposure | 0.1755 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
