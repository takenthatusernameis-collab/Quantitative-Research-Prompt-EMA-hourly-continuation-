# EMA Hourly Continuation — MOG/USDT P21_55

**Symbol:** MOG/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 875 |
| net_profit_factor | 0.6535 |
| net_win_rate | 0.4629 |
| gross_profit_factor | 0.9223 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -5.3929 |
| sortino_ratio | -2.3274 |
| max_drawdown | 0.9297 |
| cagr | -0.6804 |
| net_avg_win | 43.1813 |
| net_avg_loss | -56.9355 |
| avg_hold_time_bars | 5.4274 |
| exposure | 0.2361 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
