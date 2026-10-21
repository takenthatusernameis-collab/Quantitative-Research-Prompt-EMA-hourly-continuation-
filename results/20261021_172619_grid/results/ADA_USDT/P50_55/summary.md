# EMA Hourly Continuation — ADA/USDT P50_55

**Symbol:** ADA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 79 |
| net_profit_factor | 0.7164 |
| net_win_rate | 0.5063 |
| gross_profit_factor | 1.0121 |
| gross_win_rate | 0.5063 |
| sharpe_ratio | -0.8771 |
| sortino_ratio | -0.1122 |
| max_drawdown | 0.1296 |
| cagr | -0.0498 |
| net_avg_win | 76.0378 |
| net_avg_loss | -108.8658 |
| avg_hold_time_bars | 4.4177 |
| exposure | 0.0159 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
