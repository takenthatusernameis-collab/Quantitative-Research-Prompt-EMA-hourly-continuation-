# EMA Hourly Continuation — MASK/USDT P21_26

**Symbol:** MASK/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1187 |
| net_profit_factor | 0.1312 |
| net_win_rate | 0.3387 |
| gross_profit_factor | 0.5221 |
| gross_win_rate | 0.4195 |
| sharpe_ratio | -15.2170 |
| sortino_ratio | -7.7166 |
| max_drawdown | 1.0000 |
| cagr | -0.9843 |
| net_avg_win | 3.7559 |
| net_avg_loss | -14.6619 |
| avg_hold_time_bars | 2.5029 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
