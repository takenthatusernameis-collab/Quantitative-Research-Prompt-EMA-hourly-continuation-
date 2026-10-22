# EMA Hourly Continuation — BOSON/USDT P21_89

**Symbol:** BOSON/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 722 |
| net_profit_factor | 0.6588 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.9332 |
| gross_win_rate | 0.4668 |
| sharpe_ratio | -3.9685 |
| sortino_ratio | -1.4966 |
| max_drawdown | 0.8323 |
| cagr | -0.5081 |
| net_avg_win | 48.3573 |
| net_avg_loss | -62.4905 |
| avg_hold_time_bars | 11.3670 |
| exposure | 0.3730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
