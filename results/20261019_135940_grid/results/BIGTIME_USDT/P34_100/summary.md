# EMA Hourly Continuation — BIGTIME/USDT P34_100

**Symbol:** BIGTIME/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.6961 |
| net_win_rate | 0.4975 |
| gross_profit_factor | 1.0252 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -2.8885 |
| sortino_ratio | -0.9902 |
| max_drawdown | 0.7158 |
| cagr | -0.3741 |
| net_avg_win | 54.1973 |
| net_avg_loss | -77.0695 |
| avg_hold_time_bars | 11.4194 |
| exposure | 0.3044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
