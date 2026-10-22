# EMA Hourly Continuation — BTT/USDT P21_50

**Symbol:** BTT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1008 |
| net_profit_factor | 0.2561 |
| net_win_rate | 0.3234 |
| gross_profit_factor | 0.6703 |
| gross_win_rate | 0.3829 |
| sharpe_ratio | -14.3909 |
| sortino_ratio | -6.7580 |
| max_drawdown | 0.9999 |
| cagr | -0.9731 |
| net_avg_win | 10.5587 |
| net_avg_loss | -19.7082 |
| avg_hold_time_bars | 5.0347 |
| exposure | 0.2307 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
