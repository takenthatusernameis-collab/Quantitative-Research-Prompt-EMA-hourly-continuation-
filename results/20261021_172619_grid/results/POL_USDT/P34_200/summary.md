# EMA Hourly Continuation — POL/USDT P34_200

**Symbol:** POL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 1.0278 |
| net_win_rate | 0.5567 |
| gross_profit_factor | 1.2545 |
| gross_win_rate | 0.5567 |
| sharpe_ratio | 0.1884 |
| sortino_ratio | 0.0460 |
| max_drawdown | 0.1771 |
| cagr | 0.0144 |
| net_avg_win | 86.2558 |
| net_avg_loss | -105.4079 |
| avg_hold_time_bars | 42.9716 |
| exposure | 0.5508 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
