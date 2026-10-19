# EMA Hourly Continuation — APT/USDT P12_50

**Symbol:** APT/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1050 |
| net_profit_factor | 0.5001 |
| net_win_rate | 0.4571 |
| gross_profit_factor | 0.8646 |
| gross_win_rate | 0.4629 |
| sharpe_ratio | -6.9045 |
| sortino_ratio | -3.1265 |
| max_drawdown | 0.9811 |
| cagr | -0.7880 |
| net_avg_win | 20.4149 |
| net_avg_loss | -34.3786 |
| avg_hold_time_bars | 7.3533 |
| exposure | 0.3510 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
