# EMA Hourly Continuation — W/USDT P20_200

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.8089 |
| net_win_rate | 0.5129 |
| gross_profit_factor | 1.0618 |
| gross_win_rate | 0.5155 |
| sharpe_ratio | -1.3920 |
| sortino_ratio | -0.3856 |
| max_drawdown | 0.4681 |
| cagr | -0.1704 |
| net_avg_win | 79.6647 |
| net_avg_loss | -103.6932 |
| avg_hold_time_bars | 36.4330 |
| exposure | 0.6425 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
