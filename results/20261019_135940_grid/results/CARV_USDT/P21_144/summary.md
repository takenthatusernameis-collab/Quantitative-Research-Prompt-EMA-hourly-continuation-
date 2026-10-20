# EMA Hourly Continuation — CARV/USDT P21_144

**Symbol:** CARV/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.5824 |
| net_win_rate | 0.4521 |
| gross_profit_factor | 0.8502 |
| gross_win_rate | 0.4570 |
| sharpe_ratio | -3.8731 |
| sortino_ratio | -1.2210 |
| max_drawdown | 0.7151 |
| cagr | -0.4413 |
| net_avg_win | 52.5285 |
| net_avg_loss | -74.4171 |
| avg_hold_time_bars | 22.4668 |
| exposure | 0.5146 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
