# EMA Hourly Continuation — CRO/USDT P144_200

**Symbol:** CRO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 218 |
| net_profit_factor | 0.5827 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9042 |
| gross_win_rate | 0.4862 |
| sharpe_ratio | -2.2907 |
| sortino_ratio | -0.4850 |
| max_drawdown | 0.4484 |
| cagr | -0.1998 |
| net_avg_win | 56.4600 |
| net_avg_loss | -91.7019 |
| avg_hold_time_bars | 6.6284 |
| exposure | 0.0657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
