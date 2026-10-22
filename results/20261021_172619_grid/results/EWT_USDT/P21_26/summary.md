# EMA Hourly Continuation — EWT/USDT P21_26

**Symbol:** EWT/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 156 |
| net_profit_factor | 0.5208 |
| net_win_rate | 0.4231 |
| gross_profit_factor | 0.7136 |
| gross_win_rate | 0.4231 |
| sharpe_ratio | -2.4255 |
| sortino_ratio | -0.4296 |
| max_drawdown | 0.3938 |
| cagr | -0.1805 |
| net_avg_win | 64.7852 |
| net_avg_loss | -91.2150 |
| avg_hold_time_bars | 7.5705 |
| exposure | 0.0537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
