# EMA Hourly Continuation — MASK/USDT P8_144

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.4540 |
| net_win_rate | 0.4268 |
| gross_profit_factor | 0.7039 |
| gross_win_rate | 0.4427 |
| sharpe_ratio | -5.1016 |
| sortino_ratio | -1.7091 |
| max_drawdown | 0.8766 |
| cagr | -0.5601 |
| net_avg_win | 29.9919 |
| net_avg_loss | -49.1880 |
| avg_hold_time_bars | 27.9806 |
| exposure | 0.7211 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
