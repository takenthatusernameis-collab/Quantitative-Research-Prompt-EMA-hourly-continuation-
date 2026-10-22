# EMA Hourly Continuation — KNC/USDT P12_26

**Symbol:** KNC/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.5606 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8951 |
| gross_win_rate | 0.4473 |
| sharpe_ratio | -5.7797 |
| sortino_ratio | -2.1796 |
| max_drawdown | 0.9239 |
| cagr | -0.6355 |
| net_avg_win | 38.0179 |
| net_avg_loss | -54.5690 |
| avg_hold_time_bars | 6.1760 |
| exposure | 0.1945 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
