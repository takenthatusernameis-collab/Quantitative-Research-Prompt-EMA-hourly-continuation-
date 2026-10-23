# EMA Hourly Continuation — MOG/USDT P8_26

**Symbol:** MOG/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1397 |
| net_profit_factor | 0.6393 |
| net_win_rate | 0.4653 |
| gross_profit_factor | 0.9239 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -7.3348 |
| sortino_ratio | -4.0198 |
| max_drawdown | 0.9887 |
| cagr | -0.8581 |
| net_avg_win | 26.9618 |
| net_avg_loss | -36.6964 |
| avg_hold_time_bars | 3.9914 |
| exposure | 0.2772 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
