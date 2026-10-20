# EMA Hourly Continuation — SKL/USDT P8_26

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1644 |
| net_profit_factor | 0.4890 |
| net_win_rate | 0.4641 |
| gross_profit_factor | 0.8961 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -9.3046 |
| sortino_ratio | -5.3099 |
| max_drawdown | 0.9986 |
| cagr | -0.9262 |
| net_avg_win | 12.5253 |
| net_avg_loss | -22.1821 |
| avg_hold_time_bars | 3.5991 |
| exposure | 0.2690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
