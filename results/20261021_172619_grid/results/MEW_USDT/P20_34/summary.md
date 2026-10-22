# EMA Hourly Continuation — MEW/USDT P20_34

**Symbol:** MEW/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.6922 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9223 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -2.3088 |
| sortino_ratio | -0.6289 |
| max_drawdown | 0.5278 |
| cagr | -0.2503 |
| net_avg_win | 66.5330 |
| net_avg_loss | -88.4958 |
| avg_hold_time_bars | 5.3003 |
| exposure | 0.0875 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
