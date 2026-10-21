# EMA Hourly Continuation — AMP/USDT P50_144

**Symbol:** AMP/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 421 |
| net_profit_factor | 0.5272 |
| net_win_rate | 0.4157 |
| gross_profit_factor | 0.6838 |
| gross_win_rate | 0.4157 |
| sharpe_ratio | -3.8600 |
| sortino_ratio | -1.1206 |
| max_drawdown | 0.7465 |
| cagr | -0.4041 |
| net_avg_win | 46.3604 |
| net_avg_loss | -62.5527 |
| avg_hold_time_bars | 14.9264 |
| exposure | 0.2856 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
