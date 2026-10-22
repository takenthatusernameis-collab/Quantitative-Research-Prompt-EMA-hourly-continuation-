# EMA Hourly Continuation — MLK/USDT P8_50

**Symbol:** MLK/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.5095 |
| net_win_rate | 0.4031 |
| gross_profit_factor | 0.7183 |
| gross_win_rate | 0.4063 |
| sharpe_ratio | -5.5006 |
| sortino_ratio | -1.9545 |
| max_drawdown | 0.9028 |
| cagr | -0.5973 |
| net_avg_win | 36.4866 |
| net_avg_loss | -48.3696 |
| avg_hold_time_bars | 12.4850 |
| exposure | 0.3588 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
