# EMA Hourly Continuation — SHR/USDT P21_55

**Symbol:** SHR/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1201 |
| net_profit_factor | 0.4020 |
| net_win_rate | 0.3214 |
| gross_profit_factor | 0.6127 |
| gross_win_rate | 0.3264 |
| sharpe_ratio | -11.5416 |
| sortino_ratio | -5.6021 |
| max_drawdown | 0.9990 |
| cagr | -0.9338 |
| net_avg_win | 17.3961 |
| net_avg_loss | -20.4960 |
| avg_hold_time_bars | 4.3156 |
| exposure | 0.2345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
