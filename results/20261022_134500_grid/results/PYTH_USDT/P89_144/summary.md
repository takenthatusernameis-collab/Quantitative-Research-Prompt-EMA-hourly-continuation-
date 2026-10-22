# EMA Hourly Continuation — PYTH/USDT P89_144

**Symbol:** PYTH/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.4482 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.7830 |
| gross_win_rate | 0.4603 |
| sharpe_ratio | -4.7043 |
| sortino_ratio | -1.4930 |
| max_drawdown | 0.8423 |
| cagr | -0.5143 |
| net_avg_win | 29.8139 |
| net_avg_loss | -54.9520 |
| avg_hold_time_bars | 4.5476 |
| exposure | 0.1042 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
