# EMA Hourly Continuation — KNC/USDT P34_100

**Symbol:** KNC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.7035 |
| net_win_rate | 0.4821 |
| gross_profit_factor | 0.9754 |
| gross_win_rate | 0.4821 |
| sharpe_ratio | -2.7610 |
| sortino_ratio | -0.8353 |
| max_drawdown | 0.6713 |
| cagr | -0.3185 |
| net_avg_win | 67.9282 |
| net_avg_loss | -89.8942 |
| avg_hold_time_bars | 14.1920 |
| exposure | 0.2890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
