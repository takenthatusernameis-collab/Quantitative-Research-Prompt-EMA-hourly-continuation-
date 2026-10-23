# EMA Hourly Continuation — RIO/USDT P26_100

**Symbol:** RIO/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 800 |
| net_profit_factor | 0.5409 |
| net_win_rate | 0.4175 |
| gross_profit_factor | 0.7373 |
| gross_win_rate | 0.4200 |
| sharpe_ratio | -5.8610 |
| sortino_ratio | -2.3387 |
| max_drawdown | 0.9422 |
| cagr | -0.6739 |
| net_avg_win | 33.0927 |
| net_avg_loss | -43.8544 |
| avg_hold_time_bars | 8.7900 |
| exposure | 0.3228 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
