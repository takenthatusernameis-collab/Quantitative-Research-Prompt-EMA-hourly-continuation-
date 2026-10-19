# EMA Hourly Continuation — FLR/USDT P100_144

**Symbol:** FLR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 618 |
| net_profit_factor | 0.3372 |
| net_win_rate | 0.4045 |
| gross_profit_factor | 0.7522 |
| gross_win_rate | 0.4256 |
| sharpe_ratio | -8.0878 |
| sortino_ratio | -2.8793 |
| max_drawdown | 0.9736 |
| cagr | -0.7640 |
| net_avg_win | 19.8060 |
| net_avg_loss | -39.9059 |
| avg_hold_time_bars | 3.6472 |
| exposure | 0.1025 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
