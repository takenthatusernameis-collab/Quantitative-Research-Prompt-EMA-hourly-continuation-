# EMA Hourly Continuation — CTSI/USDT P26_55

**Symbol:** CTSI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.5212 |
| net_win_rate | 0.4351 |
| gross_profit_factor | 0.9243 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -7.5618 |
| sortino_ratio | -3.2937 |
| max_drawdown | 0.9825 |
| cagr | -0.7964 |
| net_avg_win | 25.9349 |
| net_avg_loss | -38.3207 |
| avg_hold_time_bars | 4.8891 |
| exposure | 0.2105 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
