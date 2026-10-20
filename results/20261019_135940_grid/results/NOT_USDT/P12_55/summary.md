# EMA Hourly Continuation — NOT/USDT P12_55

**Symbol:** NOT/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1020 |
| net_profit_factor | 0.5932 |
| net_win_rate | 0.4755 |
| gross_profit_factor | 0.9345 |
| gross_win_rate | 0.4853 |
| sharpe_ratio | -5.4977 |
| sortino_ratio | -2.5010 |
| max_drawdown | 0.9507 |
| cagr | -0.7031 |
| net_avg_win | 28.4942 |
| net_avg_loss | -43.5450 |
| avg_hold_time_bars | 7.7980 |
| exposure | 0.3736 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
