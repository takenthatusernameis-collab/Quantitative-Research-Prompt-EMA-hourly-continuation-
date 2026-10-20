# EMA Hourly Continuation — AIOZ/USDT P8_55

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1160 |
| net_profit_factor | 0.6808 |
| net_win_rate | 0.4733 |
| gross_profit_factor | 0.9898 |
| gross_win_rate | 0.4776 |
| sharpe_ratio | -5.6566 |
| sortino_ratio | -2.7082 |
| max_drawdown | 0.9650 |
| cagr | -0.7284 |
| net_avg_win | 37.3735 |
| net_avg_loss | -49.3276 |
| avg_hold_time_bars | 9.1698 |
| exposure | 0.4835 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
