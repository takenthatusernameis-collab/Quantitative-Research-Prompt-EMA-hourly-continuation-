# EMA Hourly Continuation — ONE/USDT P21_26

**Symbol:** ONE/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 168 |
| net_profit_factor | 0.9151 |
| net_win_rate | 0.5536 |
| gross_profit_factor | 1.2299 |
| gross_win_rate | 0.5536 |
| sharpe_ratio | -0.3235 |
| sortino_ratio | -0.0610 |
| max_drawdown | 0.1489 |
| cagr | -0.0294 |
| net_avg_win | 83.5960 |
| net_avg_loss | -113.2730 |
| avg_hold_time_bars | 4.2738 |
| exposure | 0.0326 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
