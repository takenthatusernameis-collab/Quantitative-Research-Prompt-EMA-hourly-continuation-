# EMA Hourly Continuation — FLUX/USDT P20_100

**Symbol:** FLUX/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 491 |
| net_profit_factor | 0.8274 |
| net_win_rate | 0.5092 |
| gross_profit_factor | 1.0342 |
| gross_win_rate | 0.5092 |
| sharpe_ratio | -1.2931 |
| sortino_ratio | -0.4113 |
| max_drawdown | 0.4101 |
| cagr | -0.1741 |
| net_avg_win | 73.1593 |
| net_avg_loss | -91.7227 |
| avg_hold_time_bars | 18.4134 |
| exposure | 0.4110 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
