# EMA Hourly Continuation — ANKR/USDT P21_26

**Symbol:** ANKR/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1230 |
| net_profit_factor | 0.1749 |
| net_win_rate | 0.3317 |
| gross_profit_factor | 0.5822 |
| gross_win_rate | 0.3927 |
| sharpe_ratio | -15.9226 |
| sortino_ratio | -8.2030 |
| max_drawdown | 1.0000 |
| cagr | -0.9879 |
| net_avg_win | 5.1959 |
| net_avg_loss | -14.7443 |
| avg_hold_time_bars | 2.4276 |
| exposure | 0.1357 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
