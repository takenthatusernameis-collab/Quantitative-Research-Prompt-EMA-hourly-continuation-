# EMA Hourly Continuation — WIN/USDT P55_200

**Symbol:** WIN/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 244 |
| net_profit_factor | 0.6905 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.8996 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -1.7741 |
| sortino_ratio | -0.3952 |
| max_drawdown | 0.4315 |
| cagr | -0.1671 |
| net_avg_win | 70.7905 |
| net_avg_loss | -92.9152 |
| avg_hold_time_bars | 32.0697 |
| exposure | 0.3557 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
