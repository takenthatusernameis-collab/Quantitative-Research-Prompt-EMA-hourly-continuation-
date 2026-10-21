# EMA Hourly Continuation — BCH/USDT P8_12

**Symbol:** BCH/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 204 |
| net_profit_factor | 0.5978 |
| net_win_rate | 0.4804 |
| gross_profit_factor | 0.8973 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -2.1266 |
| sortino_ratio | -0.4360 |
| max_drawdown | 0.4112 |
| cagr | -0.1792 |
| net_avg_win | 59.2934 |
| net_avg_loss | -91.7013 |
| avg_hold_time_bars | 6.0686 |
| exposure | 0.0563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
