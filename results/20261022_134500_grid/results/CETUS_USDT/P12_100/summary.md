# EMA Hourly Continuation — CETUS/USDT P12_100

**Symbol:** CETUS/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 649 |
| net_profit_factor | 0.7164 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9879 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -3.0043 |
| sortino_ratio | -1.0790 |
| max_drawdown | 0.7467 |
| cagr | -0.4023 |
| net_avg_win | 58.1227 |
| net_avg_loss | -76.9858 |
| avg_hold_time_bars | 20.4268 |
| exposure | 0.5999 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
