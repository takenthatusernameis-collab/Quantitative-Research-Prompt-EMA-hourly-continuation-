# EMA Hourly Continuation — AVAX/USDT P8_89

**Symbol:** AVAX/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 716 |
| net_profit_factor | 0.6518 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.9935 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -4.5956 |
| sortino_ratio | -1.7149 |
| max_drawdown | 0.8851 |
| cagr | -0.5681 |
| net_avg_win | 48.9469 |
| net_avg_loss | -66.3986 |
| avg_hold_time_bars | 19.2291 |
| exposure | 0.6258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
