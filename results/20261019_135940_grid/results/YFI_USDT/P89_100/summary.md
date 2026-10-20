# EMA Hourly Continuation — YFI/USDT P89_100

**Symbol:** YFI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 724 |
| net_profit_factor | 0.1790 |
| net_win_rate | 0.3287 |
| gross_profit_factor | 0.8566 |
| gross_win_rate | 0.4365 |
| sharpe_ratio | -12.1766 |
| sortino_ratio | -4.8817 |
| max_drawdown | 0.9985 |
| cagr | -0.9237 |
| net_avg_win | 9.1450 |
| net_avg_loss | -25.0233 |
| avg_hold_time_bars | 2.2790 |
| exposure | 0.0747 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
