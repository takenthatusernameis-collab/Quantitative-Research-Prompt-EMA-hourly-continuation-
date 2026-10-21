# EMA Hourly Continuation — BNB/USDT P55_89

**Symbol:** BNB/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 0.5349 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0328 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -3.1370 |
| sortino_ratio | -0.7433 |
| max_drawdown | 0.5793 |
| cagr | -0.2860 |
| net_avg_win | 49.0008 |
| net_avg_loss | -92.9869 |
| avg_hold_time_bars | 6.8910 |
| exposure | 0.0833 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
