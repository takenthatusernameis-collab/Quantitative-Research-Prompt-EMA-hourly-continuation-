# EMA Hourly Continuation — YGG/USDT P89_144

**Symbol:** YGG/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.6122 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9872 |
| gross_win_rate | 0.5042 |
| sharpe_ratio | -3.2688 |
| sortino_ratio | -1.0014 |
| max_drawdown | 0.7066 |
| cagr | -0.3808 |
| net_avg_win | 47.3330 |
| net_avg_loss | -76.0150 |
| avg_hold_time_bars | 5.5297 |
| exposure | 0.1181 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
