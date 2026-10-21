# EMA Hourly Continuation — BTC/USDT P50_55

**Symbol:** BTC/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 110 |
| net_profit_factor | 0.4618 |
| net_win_rate | 0.4727 |
| gross_profit_factor | 0.9362 |
| gross_win_rate | 0.4818 |
| sharpe_ratio | -2.2871 |
| sortino_ratio | -0.3241 |
| max_drawdown | 0.3660 |
| cagr | -0.1413 |
| net_avg_win | 58.1680 |
| net_avg_loss | -112.9197 |
| avg_hold_time_bars | 5.7909 |
| exposure | 0.0255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
