# EMA Hourly Continuation — WLD/USDT P12_100

**Symbol:** WLD/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.9490 |
| net_win_rate | 0.5247 |
| gross_profit_factor | 1.0955 |
| gross_win_rate | 0.5247 |
| sharpe_ratio | -0.2949 |
| sortino_ratio | -0.0876 |
| max_drawdown | 0.3115 |
| cagr | -0.0458 |
| net_avg_win | 92.6488 |
| net_avg_loss | -107.7747 |
| avg_hold_time_bars | 30.2188 |
| exposure | 0.5838 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
