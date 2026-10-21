# EMA Hourly Continuation — QNT/USDT P21_144

**Symbol:** QNT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.7975 |
| net_win_rate | 0.5022 |
| gross_profit_factor | 1.0169 |
| gross_win_rate | 0.5022 |
| sharpe_ratio | -1.6050 |
| sortino_ratio | -0.4892 |
| max_drawdown | 0.4931 |
| cagr | -0.2017 |
| net_avg_win | 74.9615 |
| net_avg_loss | -94.8268 |
| avg_hold_time_bars | 24.1527 |
| exposure | 0.4962 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
