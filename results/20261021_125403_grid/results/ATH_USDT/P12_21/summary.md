# EMA Hourly Continuation — ATH/USDT P12_21

**Symbol:** ATH/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.8484 |
| net_win_rate | 0.5331 |
| gross_profit_factor | 1.1327 |
| gross_win_rate | 0.5331 |
| sharpe_ratio | -0.8062 |
| sortino_ratio | -0.1930 |
| max_drawdown | 0.2170 |
| cagr | -0.0857 |
| net_avg_win | 77.7681 |
| net_avg_loss | -104.6446 |
| avg_hold_time_bars | 4.7471 |
| exposure | 0.0591 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
