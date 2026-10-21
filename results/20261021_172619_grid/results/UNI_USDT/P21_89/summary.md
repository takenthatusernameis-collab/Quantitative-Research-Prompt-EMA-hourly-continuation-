# EMA Hourly Continuation — UNI/USDT P21_89

**Symbol:** UNI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.7329 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9161 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -1.9922 |
| sortino_ratio | -0.6051 |
| max_drawdown | 0.5162 |
| cagr | -0.2428 |
| net_avg_win | 63.2761 |
| net_avg_loss | -80.0887 |
| avg_hold_time_bars | 16.7329 |
| exposure | 0.3445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
