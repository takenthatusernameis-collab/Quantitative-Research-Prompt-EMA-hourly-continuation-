# EMA Hourly Continuation — SUN/USDT P12_200

**Symbol:** SUN/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.6158 |
| net_win_rate | 0.4618 |
| gross_profit_factor | 0.8694 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -2.5287 |
| sortino_ratio | -0.5910 |
| max_drawdown | 0.5141 |
| cagr | -0.2438 |
| net_avg_win | 63.8420 |
| net_avg_loss | -88.9628 |
| avg_hold_time_bars | 59.2291 |
| exposure | 0.7371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
