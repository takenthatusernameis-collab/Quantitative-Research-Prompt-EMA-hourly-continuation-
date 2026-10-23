# EMA Hourly Continuation — W/USDT P12_55

**Symbol:** W/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 959 |
| net_profit_factor | 0.6259 |
| net_win_rate | 0.4734 |
| gross_profit_factor | 0.9355 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -4.6460 |
| sortino_ratio | -2.0222 |
| max_drawdown | 0.9161 |
| cagr | -0.6202 |
| net_avg_win | 33.6103 |
| net_avg_loss | -48.2771 |
| avg_hold_time_bars | 8.7112 |
| exposure | 0.3797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
