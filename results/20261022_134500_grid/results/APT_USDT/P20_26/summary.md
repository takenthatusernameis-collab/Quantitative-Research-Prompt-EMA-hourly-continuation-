# EMA Hourly Continuation — APT/USDT P20_26

**Symbol:** APT/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1248 |
| net_profit_factor | 0.1980 |
| net_win_rate | 0.3510 |
| gross_profit_factor | 0.6933 |
| gross_win_rate | 0.3910 |
| sharpe_ratio | -15.3035 |
| sortino_ratio | -7.8758 |
| max_drawdown | 1.0000 |
| cagr | -0.9860 |
| net_avg_win | 5.6368 |
| net_avg_loss | -15.3934 |
| avg_hold_time_bars | 1.8454 |
| exposure | 0.1047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
