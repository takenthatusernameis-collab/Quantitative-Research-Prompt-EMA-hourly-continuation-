# EMA Hourly Continuation — UNI/USDT P34_200

**Symbol:** UNI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.6040 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 0.9003 |
| gross_win_rate | 0.4771 |
| sharpe_ratio | -3.3387 |
| sortino_ratio | -0.9500 |
| max_drawdown | 0.7005 |
| cagr | -0.3720 |
| net_avg_win | 54.1760 |
| net_avg_loss | -78.7371 |
| avg_hold_time_bars | 24.3060 |
| exposure | 0.4585 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
