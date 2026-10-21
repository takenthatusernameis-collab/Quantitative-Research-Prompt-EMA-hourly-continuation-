# EMA Hourly Continuation — WOO/USDT P50_89

**Symbol:** WOO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.8424 |
| net_win_rate | 0.5332 |
| gross_profit_factor | 1.1440 |
| gross_win_rate | 0.5357 |
| sharpe_ratio | -1.0714 |
| sortino_ratio | -0.3062 |
| max_drawdown | 0.3471 |
| cagr | -0.1325 |
| net_avg_win | 76.7828 |
| net_avg_loss | -104.0994 |
| avg_hold_time_bars | 7.0918 |
| exposure | 0.1264 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
