# EMA Hourly Continuation — CARV/USDT P21_144

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.6952 |
| net_win_rate | 0.4586 |
| gross_profit_factor | 0.8571 |
| gross_win_rate | 0.4586 |
| sharpe_ratio | -2.3054 |
| sortino_ratio | -0.6450 |
| max_drawdown | 0.4918 |
| cagr | -0.2569 |
| net_avg_win | 71.6710 |
| net_avg_loss | -87.3220 |
| avg_hold_time_bars | 28.4936 |
| exposure | 0.5035 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
