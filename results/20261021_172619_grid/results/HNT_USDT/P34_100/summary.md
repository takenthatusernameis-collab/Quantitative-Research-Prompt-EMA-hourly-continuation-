# EMA Hourly Continuation — HNT/USDT P34_100

**Symbol:** HNT/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.7520 |
| net_win_rate | 0.4900 |
| gross_profit_factor | 0.9227 |
| gross_win_rate | 0.4900 |
| sharpe_ratio | -1.5722 |
| sortino_ratio | -0.4502 |
| max_drawdown | 0.4631 |
| cagr | -0.1880 |
| net_avg_win | 62.6708 |
| net_avg_loss | -80.0912 |
| avg_hold_time_bars | 14.8035 |
| exposure | 0.2705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
