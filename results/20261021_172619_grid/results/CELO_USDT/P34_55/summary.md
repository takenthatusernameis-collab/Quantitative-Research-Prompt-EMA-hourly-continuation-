# EMA Hourly Continuation — CELO/USDT P34_55

**Symbol:** CELO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 378 |
| net_profit_factor | 0.6961 |
| net_win_rate | 0.5053 |
| gross_profit_factor | 0.9894 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -2.0226 |
| sortino_ratio | -0.5641 |
| max_drawdown | 0.4979 |
| cagr | -0.2271 |
| net_avg_win | 57.3181 |
| net_avg_loss | -84.1009 |
| avg_hold_time_bars | 6.3280 |
| exposure | 0.1082 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
