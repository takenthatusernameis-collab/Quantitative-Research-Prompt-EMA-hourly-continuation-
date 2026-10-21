# EMA Hourly Continuation — APT/USDT P8_50

**Symbol:** APT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 645 |
| net_profit_factor | 0.8144 |
| net_win_rate | 0.5085 |
| gross_profit_factor | 1.0190 |
| gross_win_rate | 0.5085 |
| sharpe_ratio | -1.5301 |
| sortino_ratio | -0.5579 |
| max_drawdown | 0.5099 |
| cagr | -0.2280 |
| net_avg_win | 63.9197 |
| net_avg_loss | -81.2127 |
| avg_hold_time_bars | 14.5984 |
| exposure | 0.4280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
