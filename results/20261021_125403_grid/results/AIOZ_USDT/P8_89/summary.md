# EMA Hourly Continuation — AIOZ/USDT P8_89

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 541 |
| net_profit_factor | 0.8936 |
| net_win_rate | 0.5139 |
| gross_profit_factor | 1.0636 |
| gross_win_rate | 0.5139 |
| sharpe_ratio | -0.8925 |
| sortino_ratio | -0.2979 |
| max_drawdown | 0.4244 |
| cagr | -0.1328 |
| net_avg_win | 90.9036 |
| net_avg_loss | -107.5238 |
| avg_hold_time_bars | 24.4547 |
| exposure | 0.6014 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
