# EMA Hourly Continuation — WLD/USDT P55_144

**Symbol:** WLD/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 417 |
| net_profit_factor | 0.7357 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 0.9850 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -1.8207 |
| sortino_ratio | -0.5279 |
| max_drawdown | 0.4990 |
| cagr | -0.2203 |
| net_avg_win | 61.6027 |
| net_avg_loss | -84.9434 |
| avg_hold_time_bars | 13.6571 |
| exposure | 0.2589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
