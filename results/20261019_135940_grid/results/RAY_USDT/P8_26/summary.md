# EMA Hourly Continuation — RAY/USDT P8_26

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1513 |
| net_profit_factor | 0.5180 |
| net_win_rate | 0.4514 |
| gross_profit_factor | 0.8930 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -8.5601 |
| sortino_ratio | -4.6779 |
| max_drawdown | 0.9969 |
| cagr | -0.8992 |
| net_avg_win | 15.6856 |
| net_avg_loss | -24.9178 |
| avg_hold_time_bars | 4.0780 |
| exposure | 0.2805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
