# EMA Hourly Continuation — AGLD/USDT P21_55

**Symbol:** AGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.7054 |
| net_win_rate | 0.4671 |
| gross_profit_factor | 0.9322 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -3.3258 |
| sortino_ratio | -1.1952 |
| max_drawdown | 0.7802 |
| cagr | -0.4229 |
| net_avg_win | 60.2799 |
| net_avg_loss | -74.8937 |
| avg_hold_time_bars | 8.5000 |
| exposure | 0.2454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
