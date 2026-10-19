# EMA Hourly Continuation — ICP/USDT P21_55

**Symbol:** ICP/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 960 |
| net_profit_factor | 0.4788 |
| net_win_rate | 0.4583 |
| gross_profit_factor | 0.8565 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -6.9675 |
| sortino_ratio | -3.0386 |
| max_drawdown | 0.9770 |
| cagr | -0.7741 |
| net_avg_win | 20.3776 |
| net_avg_loss | -36.0148 |
| avg_hold_time_bars | 5.3260 |
| exposure | 0.2324 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
