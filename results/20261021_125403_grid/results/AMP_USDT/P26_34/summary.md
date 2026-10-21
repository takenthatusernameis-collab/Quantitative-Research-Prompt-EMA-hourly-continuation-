# EMA Hourly Continuation — AMP/USDT P26_34

**Symbol:** AMP/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 271 |
| net_profit_factor | 0.3348 |
| net_win_rate | 0.3321 |
| gross_profit_factor | 0.5091 |
| gross_win_rate | 0.3321 |
| sharpe_ratio | -5.4783 |
| sortino_ratio | -1.2921 |
| max_drawdown | 0.7894 |
| cagr | -0.4534 |
| net_avg_win | 43.6607 |
| net_avg_loss | -64.8393 |
| avg_hold_time_bars | 4.8118 |
| exposure | 0.0593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
