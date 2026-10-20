# EMA Hourly Continuation — ARKM/USDT P8_55

**Symbol:** ARKM/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1010 |
| net_profit_factor | 0.6589 |
| net_win_rate | 0.4802 |
| gross_profit_factor | 0.9567 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -4.5007 |
| sortino_ratio | -2.0191 |
| max_drawdown | 0.9137 |
| cagr | -0.6168 |
| net_avg_win | 36.2450 |
| net_avg_loss | -50.8180 |
| avg_hold_time_bars | 11.3614 |
| exposure | 0.5216 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
