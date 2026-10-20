# EMA Hourly Continuation — ATH/USDT P50_144

**Symbol:** ATH/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.6269 |
| net_win_rate | 0.4774 |
| gross_profit_factor | 0.9450 |
| gross_win_rate | 0.4835 |
| sharpe_ratio | -3.5571 |
| sortino_ratio | -1.1305 |
| max_drawdown | 0.7349 |
| cagr | -0.4238 |
| net_avg_win | 52.6474 |
| net_avg_loss | -76.7108 |
| avg_hold_time_bars | 11.6502 |
| exposure | 0.2744 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
