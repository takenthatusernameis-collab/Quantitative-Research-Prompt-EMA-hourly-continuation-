# EMA Hourly Continuation — XDC/USDT P20_89

**Symbol:** XDC/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7047 |
| net_win_rate | 0.5186 |
| gross_profit_factor | 1.0554 |
| gross_win_rate | 0.5186 |
| sharpe_ratio | -2.2189 |
| sortino_ratio | -0.7214 |
| max_drawdown | 0.5650 |
| cagr | -0.2795 |
| net_avg_win | 50.5266 |
| net_avg_loss | -77.2335 |
| avg_hold_time_bars | 13.3581 |
| exposure | 0.3103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
