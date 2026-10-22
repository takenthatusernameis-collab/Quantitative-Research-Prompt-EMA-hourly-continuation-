# EMA Hourly Continuation — JTO/USDT P55_100

**Symbol:** JTO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.5335 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8410 |
| gross_win_rate | 0.4547 |
| sharpe_ratio | -4.8475 |
| sortino_ratio | -1.6988 |
| max_drawdown | 0.8751 |
| cagr | -0.5578 |
| net_avg_win | 35.7112 |
| net_avg_loss | -55.0880 |
| avg_hold_time_bars | 5.1133 |
| exposure | 0.1436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
