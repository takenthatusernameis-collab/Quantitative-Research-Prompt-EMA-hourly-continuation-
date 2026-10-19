# EMA Hourly Continuation — KMNO/USDT P21_50

**Symbol:** KMNO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 835 |
| net_profit_factor | 0.5489 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.9210 |
| gross_win_rate | 0.4766 |
| sharpe_ratio | -6.0892 |
| sortino_ratio | -2.5009 |
| max_drawdown | 0.9505 |
| cagr | -0.7035 |
| net_avg_win | 30.2023 |
| net_avg_loss | -46.6207 |
| avg_hold_time_bars | 5.0659 |
| exposure | 0.1953 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
