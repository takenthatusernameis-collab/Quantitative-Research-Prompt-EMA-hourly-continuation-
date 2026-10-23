# EMA Hourly Continuation — DIA/USDT P12_200

**Symbol:** DIA/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 345 |
| net_profit_factor | 0.8888 |
| net_win_rate | 0.5362 |
| gross_profit_factor | 1.1919 |
| gross_win_rate | 0.5478 |
| sharpe_ratio | -0.5890 |
| sortino_ratio | -0.1563 |
| max_drawdown | 0.3137 |
| cagr | -0.0738 |
| net_avg_win | 75.9814 |
| net_avg_loss | -98.8424 |
| avg_hold_time_bars | 48.1507 |
| exposure | 0.7517 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
