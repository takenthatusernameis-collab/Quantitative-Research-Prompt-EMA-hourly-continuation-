# EMA Hourly Continuation — HTR/USDT P20_26

**Symbol:** HTR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1107 |
| net_profit_factor | 0.2618 |
| net_win_rate | 0.3071 |
| gross_profit_factor | 0.5810 |
| gross_win_rate | 0.3324 |
| sharpe_ratio | -14.2789 |
| sortino_ratio | -6.8303 |
| max_drawdown | 0.9999 |
| cagr | -0.9730 |
| net_avg_win | 10.4269 |
| net_avg_loss | -17.6584 |
| avg_hold_time_bars | 2.8311 |
| exposure | 0.1425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
