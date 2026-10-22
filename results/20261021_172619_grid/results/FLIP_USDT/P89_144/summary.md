# EMA Hourly Continuation — FLIP/USDT P89_144

**Symbol:** FLIP/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 206 |
| net_profit_factor | 0.4570 |
| net_win_rate | 0.4078 |
| gross_profit_factor | 0.6816 |
| gross_win_rate | 0.4078 |
| sharpe_ratio | -3.4645 |
| sortino_ratio | -0.7030 |
| max_drawdown | 0.5713 |
| cagr | -0.2829 |
| net_avg_win | 56.7346 |
| net_avg_loss | -85.4721 |
| avg_hold_time_bars | 15.3301 |
| exposure | 0.1435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
