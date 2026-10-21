# EMA Hourly Continuation — UNI/USDT P50_55

**Symbol:** UNI/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 90 |
| net_profit_factor | 0.8376 |
| net_win_rate | 0.5333 |
| gross_profit_factor | 1.1269 |
| gross_win_rate | 0.5333 |
| sharpe_ratio | -0.4781 |
| sortino_ratio | -0.0656 |
| max_drawdown | 0.1021 |
| cagr | -0.0299 |
| net_avg_win | 78.8440 |
| net_avg_loss | -107.5750 |
| avg_hold_time_bars | 5.2000 |
| exposure | 0.0213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
