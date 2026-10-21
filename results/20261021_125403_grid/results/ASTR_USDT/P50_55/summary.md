# EMA Hourly Continuation — ASTR/USDT P50_55

**Symbol:** ASTR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 176 |
| net_profit_factor | 0.6356 |
| net_win_rate | 0.5227 |
| gross_profit_factor | 1.1137 |
| gross_win_rate | 0.5227 |
| sharpe_ratio | -1.9697 |
| sortino_ratio | -0.3740 |
| max_drawdown | 0.4007 |
| cagr | -0.1618 |
| net_avg_win | 68.1525 |
| net_avg_loss | -117.4288 |
| avg_hold_time_bars | 5.2727 |
| exposure | 0.0420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
