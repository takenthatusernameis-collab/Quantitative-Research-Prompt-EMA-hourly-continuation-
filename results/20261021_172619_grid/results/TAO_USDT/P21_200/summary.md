# EMA Hourly Continuation — TAO/USDT P21_200

**Symbol:** TAO/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.9078 |
| net_win_rate | 0.5084 |
| gross_profit_factor | 1.0317 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -0.4914 |
| sortino_ratio | -0.1219 |
| max_drawdown | 0.2838 |
| cagr | -0.0577 |
| net_avg_win | 89.8452 |
| net_avg_loss | -102.3330 |
| avg_hold_time_bars | 43.6321 |
| exposure | 0.5930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
