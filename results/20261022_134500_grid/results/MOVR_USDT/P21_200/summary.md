# EMA Hourly Continuation — MOVR/USDT P21_200

**Symbol:** MOVR/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.5686 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8110 |
| gross_win_rate | 0.4487 |
| sharpe_ratio | -3.5624 |
| sortino_ratio | -1.0372 |
| max_drawdown | 0.7411 |
| cagr | -0.3971 |
| net_avg_win | 48.3746 |
| net_avg_loss | -68.6227 |
| avg_hold_time_bars | 31.7517 |
| exposure | 0.6336 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
