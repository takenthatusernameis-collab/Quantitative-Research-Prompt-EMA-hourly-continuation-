# EMA Hourly Continuation — TAO/USDT P8_200

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.8059 |
| net_win_rate | 0.5051 |
| gross_profit_factor | 1.0510 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.4629 |
| sortino_ratio | -0.4117 |
| max_drawdown | 0.4490 |
| cagr | -0.1790 |
| net_avg_win | 81.0743 |
| net_avg_loss | -102.6592 |
| avg_hold_time_bars | 44.0581 |
| exposure | 0.7930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
