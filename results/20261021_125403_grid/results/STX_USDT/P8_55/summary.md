# EMA Hourly Continuation — STX/USDT P8_55

**Symbol:** STX/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 672 |
| net_profit_factor | 0.7994 |
| net_win_rate | 0.5030 |
| gross_profit_factor | 0.9956 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -1.7618 |
| sortino_ratio | -0.6530 |
| max_drawdown | 0.5577 |
| cagr | -0.2608 |
| net_avg_win | 62.8985 |
| net_avg_loss | -79.6213 |
| avg_hold_time_bars | 15.4033 |
| exposure | 0.4684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
