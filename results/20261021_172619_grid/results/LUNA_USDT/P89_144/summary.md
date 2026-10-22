# EMA Hourly Continuation — LUNA/USDT P89_144

**Symbol:** LUNA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.6350 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8618 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -2.1116 |
| sortino_ratio | -0.4925 |
| max_drawdown | 0.4449 |
| cagr | -0.2018 |
| net_avg_win | 59.6765 |
| net_avg_loss | -84.5770 |
| avg_hold_time_bars | 8.5075 |
| exposure | 0.1029 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
