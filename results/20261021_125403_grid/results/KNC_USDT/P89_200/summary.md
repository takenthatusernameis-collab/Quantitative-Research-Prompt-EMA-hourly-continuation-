# EMA Hourly Continuation — KNC/USDT P89_200

**Symbol:** KNC/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.7834 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0619 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -1.3118 |
| sortino_ratio | -0.3153 |
| max_drawdown | 0.3869 |
| cagr | -0.1353 |
| net_avg_win | 76.8000 |
| net_avg_loss | -103.8029 |
| avg_hold_time_bars | 16.0321 |
| exposure | 0.2040 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
