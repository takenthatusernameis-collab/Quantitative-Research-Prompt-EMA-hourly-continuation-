# EMA Hourly Continuation — LTC/USDT P12_200

**Symbol:** LTC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.7312 |
| net_win_rate | 0.4871 |
| gross_profit_factor | 0.9353 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -1.3649 |
| sortino_ratio | -0.2965 |
| max_drawdown | 0.3325 |
| cagr | -0.1277 |
| net_avg_win | 69.9402 |
| net_avg_loss | -90.8231 |
| avg_hold_time_bars | 71.0948 |
| exposure | 0.7497 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
