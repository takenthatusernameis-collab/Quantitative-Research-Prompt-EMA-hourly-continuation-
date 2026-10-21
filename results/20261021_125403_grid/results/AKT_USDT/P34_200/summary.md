# EMA Hourly Continuation — AKT/USDT P34_200

**Symbol:** AKT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 316 |
| net_profit_factor | 0.8983 |
| net_win_rate | 0.5158 |
| gross_profit_factor | 1.0546 |
| gross_win_rate | 0.5158 |
| sharpe_ratio | -0.5465 |
| sortino_ratio | -0.1396 |
| max_drawdown | 0.1660 |
| cagr | -0.0656 |
| net_avg_win | 84.8316 |
| net_avg_loss | -100.6117 |
| avg_hold_time_bars | 31.5696 |
| exposure | 0.4535 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
