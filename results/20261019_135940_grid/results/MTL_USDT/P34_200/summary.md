# EMA Hourly Continuation — MTL/USDT P34_200

**Symbol:** MTL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.5706 |
| net_win_rate | 0.4475 |
| gross_profit_factor | 0.8619 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -3.4012 |
| sortino_ratio | -0.9034 |
| max_drawdown | 0.6775 |
| cagr | -0.3553 |
| net_avg_win | 54.9243 |
| net_avg_loss | -77.9682 |
| avg_hold_time_bars | 33.1022 |
| exposure | 0.5423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
