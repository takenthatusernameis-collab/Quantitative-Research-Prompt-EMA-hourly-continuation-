# EMA Hourly Continuation — 1INCH/USDT P12_50

**Symbol:** 1INCH/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1105 |
| net_profit_factor | 0.5167 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.8992 |
| gross_win_rate | 0.4670 |
| sharpe_ratio | -7.6510 |
| sortino_ratio | -3.5895 |
| max_drawdown | 0.9876 |
| cagr | -0.8247 |
| net_avg_win | 21.5869 |
| net_avg_loss | -33.1654 |
| avg_hold_time_bars | 7.2769 |
| exposure | 0.3655 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
