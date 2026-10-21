# EMA Hourly Continuation — UQC/USDT P34_200

**Symbol:** UQC/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 170 |
| net_profit_factor | 0.3578 |
| net_win_rate | 0.2941 |
| gross_profit_factor | 0.4321 |
| gross_win_rate | 0.2941 |
| sharpe_ratio | -4.1575 |
| sortino_ratio | -0.7517 |
| max_drawdown | 0.5962 |
| cagr | -0.3020 |
| net_avg_win | 66.4411 |
| net_avg_loss | -77.3631 |
| avg_hold_time_bars | 85.3000 |
| exposure | 0.6563 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
