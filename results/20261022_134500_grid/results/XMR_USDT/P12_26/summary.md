# EMA Hourly Continuation — XMR/USDT P12_26

**Symbol:** XMR/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1714 |
| net_profit_factor | 0.1534 |
| net_win_rate | 0.3483 |
| gross_profit_factor | 0.4835 |
| gross_win_rate | 0.3746 |
| sharpe_ratio | -17.2629 |
| sortino_ratio | -10.2812 |
| max_drawdown | 1.0000 |
| cagr | -0.9955 |
| net_avg_win | 3.0345 |
| net_avg_loss | -10.5744 |
| avg_hold_time_bars | 2.2375 |
| exposure | 0.1743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
