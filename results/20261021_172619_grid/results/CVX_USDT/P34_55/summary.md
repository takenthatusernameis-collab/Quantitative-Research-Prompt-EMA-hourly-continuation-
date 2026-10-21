# EMA Hourly Continuation — CVX/USDT P34_55

**Symbol:** CVX/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7467 |
| net_win_rate | 0.5057 |
| gross_profit_factor | 1.0303 |
| gross_win_rate | 0.5057 |
| sharpe_ratio | -1.7863 |
| sortino_ratio | -0.4803 |
| max_drawdown | 0.4252 |
| cagr | -0.1979 |
| net_avg_win | 70.8186 |
| net_avg_loss | -97.0325 |
| avg_hold_time_bars | 5.7000 |
| exposure | 0.0907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
