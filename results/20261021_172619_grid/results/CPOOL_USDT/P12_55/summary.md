# EMA Hourly Continuation — CPOOL/USDT P12_55

**Symbol:** CPOOL/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 620 |
| net_profit_factor | 0.8178 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9708 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -1.4684 |
| sortino_ratio | -0.5227 |
| max_drawdown | 0.4773 |
| cagr | -0.2165 |
| net_avg_win | 66.7748 |
| net_avg_loss | -80.6038 |
| avg_hold_time_bars | 11.4000 |
| exposure | 0.3213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
