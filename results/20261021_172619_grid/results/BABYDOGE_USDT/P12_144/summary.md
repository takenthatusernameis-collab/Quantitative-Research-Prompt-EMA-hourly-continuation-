# EMA Hourly Continuation — BABYDOGE/USDT P12_144

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 81 |
| net_profit_factor | 0.9157 |
| net_win_rate | 0.4938 |
| gross_profit_factor | 0.9683 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -0.2276 |
| sortino_ratio | -0.0292 |
| max_drawdown | 0.1244 |
| cagr | -0.0144 |
| net_avg_win | 97.7934 |
| net_avg_loss | -104.1876 |
| avg_hold_time_bars | 74.2099 |
| exposure | 0.2720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
