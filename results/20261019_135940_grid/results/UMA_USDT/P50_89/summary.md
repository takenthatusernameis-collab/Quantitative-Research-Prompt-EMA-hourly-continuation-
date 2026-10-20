# EMA Hourly Continuation — UMA/USDT P50_89

**Symbol:** UMA/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 681 |
| net_profit_factor | 0.5265 |
| net_win_rate | 0.4684 |
| gross_profit_factor | 0.9383 |
| gross_win_rate | 0.4831 |
| sharpe_ratio | -5.3179 |
| sortino_ratio | -1.9639 |
| max_drawdown | 0.9104 |
| cagr | -0.6116 |
| net_avg_win | 31.6154 |
| net_avg_loss | -52.9147 |
| avg_hold_time_bars | 5.7239 |
| exposure | 0.1772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
