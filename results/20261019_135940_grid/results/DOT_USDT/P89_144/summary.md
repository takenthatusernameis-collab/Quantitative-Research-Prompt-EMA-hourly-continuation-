# EMA Hourly Continuation — DOT/USDT P89_144

**Symbol:** DOT/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.4887 |
| net_win_rate | 0.4527 |
| gross_profit_factor | 0.8995 |
| gross_win_rate | 0.4615 |
| sharpe_ratio | -5.0157 |
| sortino_ratio | -1.5130 |
| max_drawdown | 0.8524 |
| cagr | -0.5259 |
| net_avg_win | 39.2767 |
| net_avg_loss | -66.4927 |
| avg_hold_time_bars | 4.3385 |
| exposure | 0.0897 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
