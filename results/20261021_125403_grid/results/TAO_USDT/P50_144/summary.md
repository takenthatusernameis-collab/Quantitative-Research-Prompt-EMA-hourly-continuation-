# EMA Hourly Continuation — TAO/USDT P50_144

**Symbol:** TAO/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.8766 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0549 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -0.6933 |
| sortino_ratio | -0.1774 |
| max_drawdown | 0.2232 |
| cagr | -0.0810 |
| net_avg_win | 83.2720 |
| net_avg_loss | -100.5442 |
| avg_hold_time_bars | 15.6972 |
| exposure | 0.2262 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
