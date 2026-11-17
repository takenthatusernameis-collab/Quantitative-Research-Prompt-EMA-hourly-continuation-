# EMA Hourly Continuation — NUM/USDT P26_89

**Symbol:** NUM/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 740 |
| net_profit_factor | 0.4870 |
| net_win_rate | 0.3797 |
| gross_profit_factor | 0.7518 |
| gross_win_rate | 0.3878 |
| sharpe_ratio | -7.2418 |
| sortino_ratio | -2.7754 |
| max_drawdown | 0.9658 |
| cagr | -0.7341 |
| net_avg_win | 32.5651 |
| net_avg_loss | -40.9405 |
| avg_hold_time_bars | 9.6041 |
| exposure | 0.3230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
