# EMA Hourly Continuation — ETN/USDT P21_200

**Symbol:** ETN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 509 |
| net_profit_factor | 0.4810 |
| net_win_rate | 0.3910 |
| gross_profit_factor | 0.6692 |
| gross_win_rate | 0.3949 |
| sharpe_ratio | -6.1575 |
| sortino_ratio | -2.1173 |
| max_drawdown | 0.8868 |
| cagr | -0.6436 |
| net_avg_win | 41.2359 |
| net_avg_loss | -55.0382 |
| avg_hold_time_bars | 18.2534 |
| exposure | 0.5047 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
