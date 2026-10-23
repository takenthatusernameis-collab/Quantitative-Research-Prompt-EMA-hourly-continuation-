# EMA Hourly Continuation — SKL/USDT P8_21

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1775 |
| net_profit_factor | 0.4470 |
| net_win_rate | 0.4558 |
| gross_profit_factor | 0.8899 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -10.7159 |
| sortino_ratio | -6.3661 |
| max_drawdown | 0.9996 |
| cagr | -0.9567 |
| net_avg_win | 9.9882 |
| net_avg_loss | -18.7129 |
| avg_hold_time_bars | 2.8028 |
| exposure | 0.2261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
