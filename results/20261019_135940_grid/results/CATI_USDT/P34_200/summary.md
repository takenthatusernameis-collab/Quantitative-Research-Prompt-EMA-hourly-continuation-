# EMA Hourly Continuation — CATI/USDT P34_200

**Symbol:** CATI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.5740 |
| net_win_rate | 0.4393 |
| gross_profit_factor | 0.8876 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -3.7009 |
| sortino_ratio | -1.0661 |
| max_drawdown | 0.6878 |
| cagr | -0.3964 |
| net_avg_win | 57.6706 |
| net_avg_loss | -78.7196 |
| avg_hold_time_bars | 29.6040 |
| exposure | 0.5615 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
