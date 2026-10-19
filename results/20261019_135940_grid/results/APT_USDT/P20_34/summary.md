# EMA Hourly Continuation — APT/USDT P20_34

**Symbol:** APT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1160 |
| net_profit_factor | 0.3018 |
| net_win_rate | 0.4129 |
| gross_profit_factor | 0.7357 |
| gross_win_rate | 0.4319 |
| sharpe_ratio | -11.1611 |
| sortino_ratio | -5.3823 |
| max_drawdown | 0.9991 |
| cagr | -0.9389 |
| net_avg_win | 9.0163 |
| net_avg_loss | -21.0130 |
| avg_hold_time_bars | 2.6897 |
| exposure | 0.1418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
