# EMA Hourly Continuation — NYM/USDT P55_144

**Symbol:** NYM/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 255 |
| net_profit_factor | 0.4247 |
| net_win_rate | 0.4039 |
| gross_profit_factor | 0.6365 |
| gross_win_rate | 0.4039 |
| sharpe_ratio | -3.8006 |
| sortino_ratio | -0.8618 |
| max_drawdown | 0.6549 |
| cagr | -0.3341 |
| net_avg_win | 45.8597 |
| net_avg_loss | -73.1718 |
| avg_hold_time_bars | 20.0431 |
| exposure | 0.2323 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
