# EMA Hourly Continuation — ENS/USDT P50_144

**Symbol:** ENS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.5289 |
| net_win_rate | 0.4582 |
| gross_profit_factor | 0.8157 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -3.9662 |
| sortino_ratio | -1.2545 |
| max_drawdown | 0.7836 |
| cagr | -0.4483 |
| net_avg_win | 37.8540 |
| net_avg_loss | -60.5171 |
| avg_hold_time_bars | 13.0498 |
| exposure | 0.2978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
