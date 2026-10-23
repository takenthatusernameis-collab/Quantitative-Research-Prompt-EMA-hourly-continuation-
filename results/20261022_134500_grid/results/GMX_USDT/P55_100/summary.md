# EMA Hourly Continuation — GMX/USDT P55_100

**Symbol:** GMX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.4873 |
| net_win_rate | 0.4505 |
| gross_profit_factor | 0.8732 |
| gross_win_rate | 0.4553 |
| sharpe_ratio | -5.7108 |
| sortino_ratio | -2.0346 |
| max_drawdown | 0.9173 |
| cagr | -0.6260 |
| net_avg_win | 30.3202 |
| net_avg_loss | -51.0167 |
| avg_hold_time_bars | 6.0047 |
| exposure | 0.1739 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
