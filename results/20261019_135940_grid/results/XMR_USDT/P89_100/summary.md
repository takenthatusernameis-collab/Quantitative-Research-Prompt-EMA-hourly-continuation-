# EMA Hourly Continuation — XMR/USDT P89_100

**Symbol:** XMR/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 895 |
| net_profit_factor | 0.1301 |
| net_win_rate | 0.2972 |
| gross_profit_factor | 0.5708 |
| gross_win_rate | 0.3385 |
| sharpe_ratio | -14.9966 |
| sortino_ratio | -6.7655 |
| max_drawdown | 0.9999 |
| cagr | -0.9766 |
| net_avg_win | 5.6230 |
| net_avg_loss | -18.2749 |
| avg_hold_time_bars | 1.6514 |
| exposure | 0.0672 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
