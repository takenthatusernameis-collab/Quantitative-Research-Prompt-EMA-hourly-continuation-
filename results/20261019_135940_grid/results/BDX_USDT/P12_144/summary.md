# EMA Hourly Continuation — BDX/USDT P12_144

**Symbol:** BDX/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1116 |
| net_profit_factor | 0.3107 |
| net_win_rate | 0.3181 |
| gross_profit_factor | 0.6593 |
| gross_win_rate | 0.3665 |
| sharpe_ratio | -14.5204 |
| sortino_ratio | -7.0136 |
| max_drawdown | 0.9999 |
| cagr | -0.9772 |
| net_avg_win | 12.6945 |
| net_avg_loss | -19.0615 |
| avg_hold_time_bars | 9.2007 |
| exposure | 0.4667 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
