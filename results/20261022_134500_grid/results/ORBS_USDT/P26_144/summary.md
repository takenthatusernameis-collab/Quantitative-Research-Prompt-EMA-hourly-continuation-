# EMA Hourly Continuation — ORBS/USDT P26_144

**Symbol:** ORBS/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 555 |
| net_profit_factor | 0.6014 |
| net_win_rate | 0.4468 |
| gross_profit_factor | 0.9127 |
| gross_win_rate | 0.4486 |
| sharpe_ratio | -4.6323 |
| sortino_ratio | -1.5335 |
| max_drawdown | 0.8480 |
| cagr | -0.5218 |
| net_avg_win | 51.2866 |
| net_avg_loss | -68.8953 |
| avg_hold_time_bars | 19.8739 |
| exposure | 0.5014 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
