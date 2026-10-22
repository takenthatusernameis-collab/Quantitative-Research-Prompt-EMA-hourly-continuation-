# EMA Hourly Continuation — KMNO/USDT P26_89

**Symbol:** KMNO/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.6262 |
| net_win_rate | 0.4673 |
| gross_profit_factor | 0.9460 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -4.0892 |
| sortino_ratio | -1.4094 |
| max_drawdown | 0.8212 |
| cagr | -0.4962 |
| net_avg_win | 49.0168 |
| net_avg_loss | -68.6789 |
| avg_hold_time_bars | 11.2161 |
| exposure | 0.3092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
