# EMA Hourly Continuation — API3/USDT P89_144

**Symbol:** API3/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 524 |
| net_profit_factor | 0.6285 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0208 |
| gross_win_rate | 0.5076 |
| sharpe_ratio | -3.4496 |
| sortino_ratio | -1.1222 |
| max_drawdown | 0.7400 |
| cagr | -0.4131 |
| net_avg_win | 47.6273 |
| net_avg_loss | -75.7822 |
| avg_hold_time_bars | 4.8034 |
| exposure | 0.1144 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
