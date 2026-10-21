# EMA Hourly Continuation — REZ/USDT P8_55

**Symbol:** REZ/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 696 |
| net_profit_factor | 0.8989 |
| net_win_rate | 0.5216 |
| gross_profit_factor | 1.0902 |
| gross_win_rate | 0.5216 |
| sharpe_ratio | -0.9561 |
| sortino_ratio | -0.3657 |
| max_drawdown | 0.4712 |
| cagr | -0.1605 |
| net_avg_win | 86.0492 |
| net_avg_loss | -104.3527 |
| avg_hold_time_bars | 14.4856 |
| exposure | 0.4651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
