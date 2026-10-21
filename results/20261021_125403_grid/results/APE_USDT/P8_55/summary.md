# EMA Hourly Continuation — APE/USDT P8_55

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 673 |
| net_profit_factor | 0.7194 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4621 |
| sharpe_ratio | -3.1473 |
| sortino_ratio | -1.1610 |
| max_drawdown | 0.7524 |
| cagr | -0.4132 |
| net_avg_win | 60.8072 |
| net_avg_loss | -72.6209 |
| avg_hold_time_bars | 14.6196 |
| exposure | 0.4472 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
