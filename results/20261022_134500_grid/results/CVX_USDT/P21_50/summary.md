# EMA Hourly Continuation — CVX/USDT P21_50

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.4865 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8224 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -6.8684 |
| sortino_ratio | -3.0171 |
| max_drawdown | 0.9754 |
| cagr | -0.7698 |
| net_avg_win | 21.3307 |
| net_avg_loss | -35.2903 |
| avg_hold_time_bars | 4.6292 |
| exposure | 0.2043 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
