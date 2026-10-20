# EMA Hourly Continuation — UMA/USDT P34_200

**Symbol:** UMA/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.6138 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.8850 |
| gross_win_rate | 0.4775 |
| sharpe_ratio | -3.0229 |
| sortino_ratio | -0.8953 |
| max_drawdown | 0.6672 |
| cagr | -0.3459 |
| net_avg_win | 49.6266 |
| net_avg_loss | -72.5573 |
| avg_hold_time_bars | 24.0856 |
| exposure | 0.4861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
