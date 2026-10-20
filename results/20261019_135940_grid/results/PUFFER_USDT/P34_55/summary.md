# EMA Hourly Continuation — PUFFER/USDT P34_55

**Symbol:** PUFFER/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 648 |
| net_profit_factor | 0.5889 |
| net_win_rate | 0.4877 |
| gross_profit_factor | 1.0267 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -5.0418 |
| sortino_ratio | -2.0188 |
| max_drawdown | 0.8618 |
| cagr | -0.6236 |
| net_avg_win | 39.0212 |
| net_avg_loss | -63.0642 |
| avg_hold_time_bars | 3.8735 |
| exposure | 0.1420 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
