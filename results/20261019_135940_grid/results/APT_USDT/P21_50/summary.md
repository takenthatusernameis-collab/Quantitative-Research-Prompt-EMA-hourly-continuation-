# EMA Hourly Continuation — APT/USDT P21_50

**Symbol:** APT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1023 |
| net_profit_factor | 0.4552 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4673 |
| sharpe_ratio | -7.4069 |
| sortino_ratio | -3.3543 |
| max_drawdown | 0.9849 |
| cagr | -0.8052 |
| net_avg_win | 17.6699 |
| net_avg_loss | -32.3515 |
| avg_hold_time_bars | 4.3245 |
| exposure | 0.2011 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
