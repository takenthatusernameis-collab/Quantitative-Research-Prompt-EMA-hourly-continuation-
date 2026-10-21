# EMA Hourly Continuation — ENA/USDT P8_50

**Symbol:** ENA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.9311 |
| net_win_rate | 0.5242 |
| gross_profit_factor | 1.0915 |
| gross_win_rate | 0.5242 |
| sharpe_ratio | -0.5174 |
| sortino_ratio | -0.1916 |
| max_drawdown | 0.3451 |
| cagr | -0.0925 |
| net_avg_win | 84.5066 |
| net_avg_loss | -100.0084 |
| avg_hold_time_bars | 13.6227 |
| exposure | 0.4087 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
