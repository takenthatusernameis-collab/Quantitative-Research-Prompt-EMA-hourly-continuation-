# EMA Hourly Continuation — CYBER/USDT P20_144

**Symbol:** CYBER/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.6924 |
| net_win_rate | 0.4890 |
| gross_profit_factor | 0.9738 |
| gross_win_rate | 0.4912 |
| sharpe_ratio | -2.4846 |
| sortino_ratio | -0.7427 |
| max_drawdown | 0.6003 |
| cagr | -0.3013 |
| net_avg_win | 59.9154 |
| net_avg_loss | -82.8179 |
| avg_hold_time_bars | 28.6031 |
| exposure | 0.5929 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
