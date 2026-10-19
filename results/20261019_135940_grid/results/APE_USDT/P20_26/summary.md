# EMA Hourly Continuation — APE/USDT P20_26

**Symbol:** APE/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1187 |
| net_profit_factor | 0.1770 |
| net_win_rate | 0.3547 |
| gross_profit_factor | 0.6094 |
| gross_win_rate | 0.4027 |
| sharpe_ratio | -14.4378 |
| sortino_ratio | -7.1937 |
| max_drawdown | 0.9999 |
| cagr | -0.9794 |
| net_avg_win | 5.1073 |
| net_avg_loss | -15.8611 |
| avg_hold_time_bars | 1.7784 |
| exposure | 0.0960 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
