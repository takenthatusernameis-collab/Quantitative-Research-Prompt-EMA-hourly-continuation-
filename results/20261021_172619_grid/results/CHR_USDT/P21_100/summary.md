# EMA Hourly Continuation — CHR/USDT P21_100

**Symbol:** CHR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.7323 |
| net_win_rate | 0.4677 |
| gross_profit_factor | 0.8948 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -2.3946 |
| sortino_ratio | -0.7793 |
| max_drawdown | 0.6454 |
| cagr | -0.3016 |
| net_avg_win | 66.2534 |
| net_avg_loss | -79.4829 |
| avg_hold_time_bars | 16.8023 |
| exposure | 0.3999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
