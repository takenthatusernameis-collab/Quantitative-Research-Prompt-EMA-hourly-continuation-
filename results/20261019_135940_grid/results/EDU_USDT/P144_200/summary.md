# EMA Hourly Continuation — EDU/USDT P144_200

**Symbol:** EDU/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 420 |
| net_profit_factor | 0.5164 |
| net_win_rate | 0.4381 |
| gross_profit_factor | 0.8534 |
| gross_win_rate | 0.4476 |
| sharpe_ratio | -4.5166 |
| sortino_ratio | -1.3147 |
| max_drawdown | 0.7958 |
| cagr | -0.4635 |
| net_avg_win | 45.9652 |
| net_avg_loss | -69.4006 |
| avg_hold_time_bars | 4.6952 |
| exposure | 0.0892 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
