# EMA Hourly Continuation — SQD/USDT P100_144

**Symbol:** SQD/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 242 |
| net_profit_factor | 0.7586 |
| net_win_rate | 0.4835 |
| gross_profit_factor | 0.9429 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -1.3831 |
| sortino_ratio | -0.3121 |
| max_drawdown | 0.3118 |
| cagr | -0.1341 |
| net_avg_win | 79.2777 |
| net_avg_loss | -97.8109 |
| avg_hold_time_bars | 7.1983 |
| exposure | 0.0819 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
