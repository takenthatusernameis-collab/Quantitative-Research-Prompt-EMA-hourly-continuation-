# EMA Hourly Continuation — STRK/USDT P8_89

**Symbol:** STRK/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.6870 |
| net_win_rate | 0.4927 |
| gross_profit_factor | 0.9999 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -3.1019 |
| sortino_ratio | -1.1370 |
| max_drawdown | 0.7571 |
| cagr | -0.4220 |
| net_avg_win | 48.5353 |
| net_avg_loss | -68.6227 |
| avg_hold_time_bars | 20.7099 |
| exposure | 0.6458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
