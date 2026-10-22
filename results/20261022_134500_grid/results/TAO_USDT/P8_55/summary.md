# EMA Hourly Continuation — TAO/USDT P8_55

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1058 |
| net_profit_factor | 0.7167 |
| net_win_rate | 0.4924 |
| gross_profit_factor | 1.0444 |
| gross_win_rate | 0.4981 |
| sharpe_ratio | -4.3853 |
| sortino_ratio | -2.0074 |
| max_drawdown | 0.9168 |
| cagr | -0.6190 |
| net_avg_win | 44.2551 |
| net_avg_loss | -59.9083 |
| avg_hold_time_bars | 10.0435 |
| exposure | 0.4830 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
