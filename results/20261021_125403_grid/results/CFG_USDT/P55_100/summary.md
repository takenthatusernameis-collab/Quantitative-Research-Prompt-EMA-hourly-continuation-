# EMA Hourly Continuation — CFG/USDT P55_100

**Symbol:** CFG/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 346 |
| net_profit_factor | 0.7618 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9680 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -1.5486 |
| sortino_ratio | -0.4116 |
| max_drawdown | 0.4144 |
| cagr | -0.1723 |
| net_avg_win | 70.6935 |
| net_avg_loss | -90.6816 |
| avg_hold_time_bars | 7.3295 |
| exposure | 0.1153 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
