# EMA Hourly Continuation — HTR/USDT P21_144

**Symbol:** HTR/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 658 |
| net_profit_factor | 0.5345 |
| net_win_rate | 0.4195 |
| gross_profit_factor | 0.7578 |
| gross_win_rate | 0.4225 |
| sharpe_ratio | -5.5736 |
| sortino_ratio | -2.0023 |
| max_drawdown | 0.9150 |
| cagr | -0.6224 |
| net_avg_win | 37.9965 |
| net_avg_loss | -51.3618 |
| avg_hold_time_bars | 15.7021 |
| exposure | 0.4696 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
