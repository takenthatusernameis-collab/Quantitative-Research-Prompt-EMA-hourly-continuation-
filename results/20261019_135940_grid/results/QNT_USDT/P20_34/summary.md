# EMA Hourly Continuation — QNT/USDT P20_34

**Symbol:** QNT/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1251 |
| net_profit_factor | 0.2425 |
| net_win_rate | 0.4141 |
| gross_profit_factor | 0.7115 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -12.2882 |
| sortino_ratio | -6.2150 |
| max_drawdown | 0.9997 |
| cagr | -0.9606 |
| net_avg_win | 6.1790 |
| net_avg_loss | -18.0051 |
| avg_hold_time_bars | 2.4149 |
| exposure | 0.1373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
