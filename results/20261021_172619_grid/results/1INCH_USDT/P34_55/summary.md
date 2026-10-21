# EMA Hourly Continuation — 1INCH/USDT P34_55

**Symbol:** 1INCH/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.5974 |
| net_win_rate | 0.4711 |
| gross_profit_factor | 0.8783 |
| gross_win_rate | 0.4711 |
| sharpe_ratio | -3.0679 |
| sortino_ratio | -0.8379 |
| max_drawdown | 0.6215 |
| cagr | -0.3182 |
| net_avg_win | 53.6125 |
| net_avg_loss | -79.9276 |
| avg_hold_time_bars | 5.2479 |
| exposure | 0.0866 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
