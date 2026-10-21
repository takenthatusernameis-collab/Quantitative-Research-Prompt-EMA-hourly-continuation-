# EMA Hourly Continuation — WIF/USDT P34_100

**Symbol:** WIF/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.8498 |
| net_win_rate | 0.5074 |
| gross_profit_factor | 1.0214 |
| gross_win_rate | 0.5074 |
| sharpe_ratio | -1.0227 |
| sortino_ratio | -0.2948 |
| max_drawdown | 0.3524 |
| cagr | -0.1291 |
| net_avg_win | 80.9093 |
| net_avg_loss | -98.0860 |
| avg_hold_time_bars | 12.7178 |
| exposure | 0.2335 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
