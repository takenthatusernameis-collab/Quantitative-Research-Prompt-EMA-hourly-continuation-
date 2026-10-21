# EMA Hourly Continuation — TAO/USDT P89_200

**Symbol:** TAO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 229 |
| net_profit_factor | 0.8060 |
| net_win_rate | 0.4978 |
| gross_profit_factor | 0.9752 |
| gross_win_rate | 0.4978 |
| sharpe_ratio | -0.9899 |
| sortino_ratio | -0.2140 |
| max_drawdown | 0.2211 |
| cagr | -0.0944 |
| net_avg_win | 80.3547 |
| net_avg_loss | -98.8308 |
| avg_hold_time_bars | 15.2751 |
| exposure | 0.1590 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
