# EMA Hourly Continuation — GALA/USDT P8_12

**Symbol:** GALA/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1843 |
| net_profit_factor | 0.2189 |
| net_win_rate | 0.3738 |
| gross_profit_factor | 0.6332 |
| gross_win_rate | 0.4102 |
| sharpe_ratio | -17.1059 |
| sortino_ratio | -10.5618 |
| max_drawdown | 1.0000 |
| cagr | -0.9962 |
| net_avg_win | 4.0670 |
| net_avg_loss | -11.0937 |
| avg_hold_time_bars | 1.8226 |
| exposure | 0.1527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
