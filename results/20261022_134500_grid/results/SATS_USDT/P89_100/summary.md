# EMA Hourly Continuation — SATS/USDT P89_100

**Symbol:** SATS/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 450 |
| net_profit_factor | 0.3018 |
| net_win_rate | 0.3889 |
| gross_profit_factor | 0.6829 |
| gross_win_rate | 0.4067 |
| sharpe_ratio | -6.9953 |
| sortino_ratio | -2.1227 |
| max_drawdown | 0.9330 |
| cagr | -0.6528 |
| net_avg_win | 22.9865 |
| net_avg_loss | -48.4698 |
| avg_hold_time_bars | 2.7111 |
| exposure | 0.0552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
