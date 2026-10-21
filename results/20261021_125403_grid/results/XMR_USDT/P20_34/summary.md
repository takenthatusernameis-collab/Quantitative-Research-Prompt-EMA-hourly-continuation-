# EMA Hourly Continuation — XMR/USDT P20_34

**Symbol:** XMR/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 200 |
| net_profit_factor | 0.4561 |
| net_win_rate | 0.4000 |
| gross_profit_factor | 0.6501 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -3.2771 |
| sortino_ratio | -0.6578 |
| max_drawdown | 0.5397 |
| cagr | -0.2618 |
| net_avg_win | 55.9055 |
| net_avg_loss | -81.7185 |
| avg_hold_time_bars | 4.7900 |
| exposure | 0.0435 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
