# EMA Hourly Continuation — GTC/USDT P20_50

**Symbol:** GTC/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 936 |
| net_profit_factor | 0.4860 |
| net_win_rate | 0.4370 |
| gross_profit_factor | 0.8662 |
| gross_win_rate | 0.4509 |
| sharpe_ratio | -7.1857 |
| sortino_ratio | -3.0841 |
| max_drawdown | 0.9779 |
| cagr | -0.7782 |
| net_avg_win | 22.5919 |
| net_avg_loss | -36.0764 |
| avg_hold_time_bars | 5.5118 |
| exposure | 0.2345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
