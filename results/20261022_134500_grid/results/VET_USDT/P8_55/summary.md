# EMA Hourly Continuation — VET/USDT P8_55

**Symbol:** VET/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1034 |
| net_profit_factor | 0.5577 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.9595 |
| gross_win_rate | 0.4797 |
| sharpe_ratio | -6.3104 |
| sortino_ratio | -2.8490 |
| max_drawdown | 0.9702 |
| cagr | -0.7505 |
| net_avg_win | 25.3633 |
| net_avg_loss | -39.7082 |
| avg_hold_time_bars | 10.0580 |
| exposure | 0.4727 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
