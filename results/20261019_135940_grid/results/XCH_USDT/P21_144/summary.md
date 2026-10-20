# EMA Hourly Continuation — XCH/USDT P21_144

**Symbol:** XCH/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 635 |
| net_profit_factor | 0.6194 |
| net_win_rate | 0.4772 |
| gross_profit_factor | 0.9739 |
| gross_win_rate | 0.4898 |
| sharpe_ratio | -3.4875 |
| sortino_ratio | -1.2333 |
| max_drawdown | 0.7814 |
| cagr | -0.4476 |
| net_avg_win | 41.6180 |
| net_avg_loss | -61.3184 |
| avg_hold_time_bars | 18.2346 |
| exposure | 0.5263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
