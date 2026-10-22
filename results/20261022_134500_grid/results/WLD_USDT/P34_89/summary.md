# EMA Hourly Continuation — WLD/USDT P34_89

**Symbol:** WLD/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.6878 |
| net_win_rate | 0.5024 |
| gross_profit_factor | 1.0062 |
| gross_win_rate | 0.5088 |
| sharpe_ratio | -2.7497 |
| sortino_ratio | -0.9720 |
| max_drawdown | 0.6919 |
| cagr | -0.3711 |
| net_avg_win | 48.1264 |
| net_avg_loss | -70.6391 |
| avg_hold_time_bars | 8.1228 |
| exposure | 0.2315 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
